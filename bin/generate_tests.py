
import json

class TestWriter(object):
    def __init__(self, import_fname):
        super().__init__()
        self.import_fname = import_fname
        # TODO: Improve paths
        self.test_folder_name = "tests"
        self.test_file_format = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################
## NOTE: This module was autogenerated. ##
## Contains no user-servicable parts!!! ##
##########################################

# Temporary imports for hack, will be reworked once this becomes a package!!!
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..')) 
# End of hack

import unittest

from {import_fname} import {test_function}

class Test{test_name_pascal}(unittest.TestCase):
    # test_args has the format [{{
    #    "in":     ..., # (required)
    #    "out":    ..., # (required)
    #    "desc":   ..., # (optional) 
    #    "kwargs": ...  # (optional)
    # }}, ...
    # ]
    test_args = {test_args}

    def test_{test_function}(self):
        for test_case in self.test_args:
            with self.subTest():
                # Expand test_case with default cases, if optional keys are not provided
                test_case = {{**test_case, **{{
                    "desc": f"{test_function}({{repr(test_case['in'])}}) => {{repr(test_case['out'])}}",
                    "kwargs": dict()
                }}}}
                self.assertEqual({test_function}(test_case["in"], **test_case["kwargs"]), test_case["out"], test_case["desc"])

if __name__ == "__main__":
    unittest.main()
"""
    
    def _format_test_args(self, test_args):
        """
        Give test_args a nicer formatting.
        Note that we don't use json.dumps as it will eg. turn "True" into "true".

        This also removes duplicates
        """
        return "[\n" + "".join(sorted({f"        {test_case},\n" for test_case in test_args})) + "    ]"

    def write_test(self, test_path, test_function, test_name_pascal, test_args):
        with open(test_path, "w+") as f:
            f.write(self.test_file_format.format(import_fname=self.import_fname,
                                                 test_function=test_function,
                                                 test_name_pascal=test_name_pascal,
                                                 test_args=self._format_test_args(test_args)))
