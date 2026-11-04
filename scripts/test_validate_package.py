"""Regression checks for fixed tables and optional subjective system expansions."""
import tempfile
import unittest
from pathlib import Path

import validate_package as validator


class TableOutputTests(unittest.TestCase):
    def setUp(self):
        self.contract = validator.contracts()

    def table(self, key):
        headers, rows = self.contract[key]
        lines = [f'# {validator.TITLES[key]}',
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
            blocks.extend([self.table('table-1-1'), self.table('table-1-2')])
            if expansion:
                blocks.append(f'### System expansion — S{symptom} — Nervous system — Candidate A\n'
                              '| Analysis item | Content |\n| --- | --- |\n'
                              '| Pathway | Pending clarification. |')
                blocks.append(f'### System expansion — S{symptom} — Vessels — Candidate B\n'
                              '- Relationship remains unconfirmed.')
        if complete:
            blocks.extend(self.table(key) for key in validator.MODES['complete'][2:])
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
        self.assertEqual(self.check(self.output(2, True, True), 2, 'complete'), 9)

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

    def test_objective_output_alone_is_unchanged(self):
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


if __name__ == '__main__':
    unittest.main()
