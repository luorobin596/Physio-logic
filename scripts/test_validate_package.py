"""Regression checks for fixed tables and optional subjective system expansions."""
import tempfile
import unittest
from pathlib import Path

import validate_package as validator


class TableOutputTests(unittest.TestCase):
    def setUp(self):
        self.contract = validator.contracts()

    def table(self, key, symptom=1):
        headers, rows = self.contract[key]
        title = validator.TITLES[key]
        if key in validator.PER_SYMPTOM:
            number = key.removeprefix('table-').replace('-', '.')
            title = title.replace(number, f'{number}.{symptom}', 1) + f' — S{symptom}'
        lines = [f'# {title}',
                 '| ' + ' | '.join(headers) + ' |',
                 '| ' + ' | '.join(['---'] * len(headers)) + ' |']
        for name in (['Reported event'] if key == 'table-2-2' else rows):
            values = [name] + ['Unable to determine.'] * (len(headers) - 1)
            if key in ('table-3-1', 'table-3-2'):
                values[-1] = '? Unable to determine / Pending assessment — not assessed.'
            lines.append('| ' + ' | '.join(values) + ' |')
        return '\n'.join(lines)

    def output(self, symptoms=1, expansion=False, complete=False):
        blocks = []
        for symptom in range(1, symptoms + 1):
            blocks.extend([self.table('table-1-1', symptom), self.table('table-1-2', symptom)])
            if expansion:
                blocks.append(f'### System expansion — S{symptom} — Nervous system — Candidate A\n'
                              '| Analysis item | Content |\n| --- | --- |\n'
                              '| Pathway | Pending clarification. |')
                blocks.append(f'### System expansion — S{symptom} — Vessels — Candidate B\n'
                              '- Relationship remains unconfirmed.')
        if complete:
            for key in validator.MODES['complete'][2:]:
                count = symptoms if key in validator.PER_SYMPTOM else 1
                blocks.extend(self.table(key, symptom) for symptom in range(1, count + 1))
            blocks.append('Prognosis: Unable to determine.\nRed flags: Not assessed.')
        blocks.extend(f'# {heading}\nNot assessed.' for heading in
                      ('Red Flags', 'Yellow Flags', 'Reasoning Rationale and Limitations'))
        return '\n\n'.join(blocks)

    def check(self, body, symptoms=1, mode='subjective-initial'):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'output.md'
            path.write_text(body)
            return validator.validate_output(path, mode, symptoms, self.contract)

    def test_subjective_contract_and_objective_contract_are_separate(self):
        self.assertEqual(self.contract['table-1-2'][0],
                         ['System / Category', 'Explanation & Basis', 'Structures & Relationships'])
        self.assertIn('Myofascial / Fascial system', self.contract['table-1-2'][1])
        self.assertEqual(self.contract['table-3-2'][0],
                         ['Integrated functions or Systems', 'Upstream and Downstream',
                          'Regions', 'Supporting evidence', 'Possibility of Involvement'])
        self.assertIn('Myofascial lines', self.contract['table-3-2'][1])

    def test_without_expansion(self):
        self.assertEqual(self.check(self.output()), 2)

    def test_expansion_does_not_count_as_fixed_table(self):
        self.assertEqual(self.check(self.output(expansion=True)), 2)

    def test_multiple_symptom_blocks_with_expansions(self):
        self.assertEqual(self.check(self.output(2, expansion=True), symptoms=2), 4)

    def test_complete_output_resumes_fixed_tables_after_expansion(self):
        self.assertEqual(self.check(self.output(2, True, True), 2, 'complete'), 12)

    def test_wrong_header_still_fails(self):
        body = self.output(expansion=True).replace('Structures & Relationships', 'Wrong header')
        with self.assertRaisesRegex(ValueError, 'incorrect headers'):
            self.check(body)

    def test_missing_base_row_still_fails(self):
        body = '\n'.join(line for line in self.output().splitlines()
                         if not line.startswith('| lymphatic system |'))
        with self.assertRaisesRegex(ValueError, 'base rows'):
            self.check(body)

    def test_old_subjective_header_is_rejected(self):
        body = self.output().replace(
            'System / Category | Explanation & Basis | Structures & Relationships',
            'Integrated functions or Systems | Upstream and Downstream structure | Regions This System Passes Through')
        with self.assertRaisesRegex(ValueError, 'incorrect headers'):
            self.check(body)

    def test_old_subjective_category_is_rejected(self):
        body = self.output().replace('Myofascial / Fascial system', 'Myofascial lines')
        with self.assertRaisesRegex(ValueError, 'base rows'):
            self.check(body)

    def test_fixed_table_errors_after_expansion_are_not_ignored(self):
        body = self.output(expansion=True, complete=True).replace(
            'Supporting evidence | Possibility of Involvement',
            'Wrong evidence header | Possibility of Involvement')
        with self.assertRaisesRegex(ValueError, 'incorrect headers'):
            self.check(body, mode='complete')

    def test_missing_repeated_symptom_pair_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'order|repetition count'):
            self.check(self.output(expansion=True), symptoms=2)

    def test_objective_output_alone_uses_numbered_symptom_titles(self):
        body = '\n\n'.join([self.table('table-3-1'), self.table('table-3-2'),
                             '# Red Flags', '# Yellow Flags', '# Reasoning Rationale and Limitations'])
        self.assertEqual(self.check(body, mode='objective'), 2)

    def test_missing_fixed_table_after_expansion_still_fails(self):
        body = self.output(expansion=True) + '\n\n' + self.table('table-2-1')
        with self.assertRaisesRegex(ValueError, 'expected'):
            self.check(body, mode='complete')

    def test_reversed_subjective_pair_still_fails(self):
        body = '\n\n'.join([self.table('table-1-2'), self.table('table-1-1'),
                             '# Red Flags', '# Yellow Flags', '# Reasoning Rationale and Limitations'])
        with self.assertRaisesRegex(ValueError, 'order'):
            self.check(body)


    def test_synthesis_has_profiles_per_symptom_and_one_timeline(self):
        body = '\n\n'.join([self.table('table-2-1', 1), self.table('table-2-1', 2),
                               self.table('table-2-2'), '# Red Flags', '# Yellow Flags',
                               '# Reasoning Rationale and Limitations'])
        self.assertEqual(self.check(body, 2, 'subjective-synthesis'), 3)
        with self.assertRaisesRegex(ValueError, 'repetition count'):
            self.check(body + '\n\n' + self.table('table-2-2'), 2, 'subjective-synthesis')

    def test_objective_tables_repeat_per_symptom(self):
        body = '\n\n'.join([self.table(key, symptom)
                               for key in ('table-3-1', 'table-3-2') for symptom in (1, 2)] +
                              ['# Red Flags', '# Yellow Flags', '# Reasoning Rationale and Limitations'])
        self.assertEqual(self.check(body, 2, 'objective'), 4)

    def test_mismatched_symptom_mapping_is_rejected(self):
        body = self.output(2, complete=True).replace(
            'Table2.1.2 Preliminary Hypothesis — S2', 'Table2.1.2 Preliminary Hypothesis — S9')
        with self.assertRaisesRegex(ValueError, 'mapping differs'):
            self.check(body, 2, 'complete')

    def test_duplicate_instance_is_rejected(self):
        body = self.output(2).replace('Table 1.1.2', 'Table 1.1.1')
        with self.assertRaisesRegex(ValueError, 'duplicate instance'):
            self.check(body, 2)

    def test_unnumbered_output_title_is_rejected(self):
        body = self.output().replace(
            'Subjective Table 1.1.1 — S1', 'Subjective Table 1.1')
        with self.assertRaisesRegex(ValueError, 'numbered titles'):
            self.check(body)

    def test_subjective_impression_row_is_rejected(self):
        body = self.output(complete=True).replace('| Hypothesis |', '| Impression |')
        with self.assertRaisesRegex(ValueError, 'base rows'):
            self.check(body, mode='complete')


if __name__ == '__main__':
    unittest.main()
