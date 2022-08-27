import unittest
from sys import path
from pathlib import Path
from rapydmain import rapydmain
from logging import Logger, getLogger, config as loggingConfig
from logging.handlers import MemoryHandler
from io import StringIO
import sys
import re
import os
import shutil

class TestRapydmain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _clean_dirs(self, dir_path_list: list) -> None:
        for dir_path in dir_path_list:
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)

    def test_init_fw_dir_missing(self):
        with self.assertRaises(FileNotFoundError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_fw_dir_missing', 'missing_dir_root'))
        self.assertEqual(e.exception.args[0], "dir '[root_path]/' does not exists.")

        with self.assertRaises(FileNotFoundError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_fw_dir_missing', 'missing_dir_config'))
        self.assertEqual(e.exception.args[0], "dir '[root_path]/config/' does not exists.")

        with self.assertRaises(FileNotFoundError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_fw_dir_missing', 'missing_dir_log'))
        self.assertEqual(e.exception.args[0], "dir '[root_path]/log/' does not exists.")

    def test_init_config_file_missing(self):
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_file_missing', 'missing_config_fw'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_file_missing', 'missing_config_logger'))
        self.assertEqual(e.exception.args[0], "Missing dict key['logger']")

    def test_init_config_property_missing(self):
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_app'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['app']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_app_name'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['app']['name']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_message'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['message']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_message_begin'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['message']['begin']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_message_end'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['message']['end']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_message_error'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['message']['error']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_logger'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['logger']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_logger_logger_enables'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['logger']['logger_enables']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_logger_log_file_name_format'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['logger']['log_file_name_format']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_fw_logger_log_file_extension'))
        self.assertEqual(e.exception.args[0], "Missing dict key['fw']['logger']['log_file_extension']")
        with self.assertRaises(KeyError) as e:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_logger&enables_true'))
        self.assertEqual(e.exception.args[0], "Missing dict key['logger']")
        try:
            rapydmain(Path(__file__).parent / Path('test_init_config_property_missing', 'missing_config_logger&enables_false'))
        except:
            self.fail()

    def test_init_app_name(self):
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_1'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_2'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_3'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_4'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_5'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()
        try:
            main = rapydmain(Path(__file__).parent / Path('test_init_app_name', 'app_name_6'))
            self.assertIsInstance(main, rapydmain)
        except:
            self.fail()

    def test_init_config_property_fw_logger_logger_enables(self):
        with rapydmain(Path(__file__).parent / Path('test_init_config_property', 'fw_logger_logger_enables', 'logger_enables_true')) as main:
            self.assertIsInstance(main.logger, Logger)

        with rapydmain(Path(__file__).parent / Path('test_init_config_property', 'fw_logger_logger_enables', 'logger_enables_false')) as main:
            self.assertTrue(main.logger is None)

        with rapydmain(Path(__file__).parent / Path('test_init_config_property', 'fw_logger_logger_enables', 'logger_enables_not_boolean1')) as main:
            self.assertTrue(main.logger is None)

        with rapydmain(Path(__file__).parent / Path('test_init_config_property', 'fw_logger_logger_enables', 'logger_enables_not_boolean2')) as main:
            self.assertTrue(main.logger is None)

    def test_init_config_property_fw_logger_output_begin_message_enables(self):
        # setup
        fw_root_dir1 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_begin_message_enables', 'output_begin_message_enables_true')
        fw_root_dir2 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_begin_message_enables', 'output_begin_message_enables_false')
        fw_root_dir3 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_begin_message_enables', 'output_begin_message_enables_not_boolean1')
        fw_root_dir4 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_begin_message_enables', 'output_begin_message_enables_not_boolean2')
        self._clean_dirs([
            fw_root_dir1 / Path('log'),
            fw_root_dir2 / Path('log'),
            fw_root_dir3 / Path('log'),
            fw_root_dir4 / Path('log')
        ])

        # test
        with rapydmain(fw_root_dir1) as main:
            with open(main.log_file_path()) as f:
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                    f.read()
                ))

        with rapydmain(fw_root_dir2) as main:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                    f.read()
                ))

        with rapydmain(fw_root_dir3) as main:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                    f.read()
                ))

        with rapydmain(fw_root_dir4) as main:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                    f.read()
                ))

    def test_init_config_property_fw_logger_output_end_message_enables(self):
        # setup
        fw_root_dir1 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_end_message_enables', 'output_end_message_enables_true')
        fw_root_dir2 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_end_message_enables', 'output_end_message_enables_false')
        fw_root_dir3 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_end_message_enables', 'output_end_message_enables_not_boolean1')
        fw_root_dir4 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_end_message_enables', 'output_end_message_enables_not_boolean2')
        self._clean_dirs([
            fw_root_dir1 / Path('log'),
            fw_root_dir2 / Path('log'),
            fw_root_dir3 / Path('log'),
            fw_root_dir4 / Path('log')
        ])

        # test
        with rapydmain(fw_root_dir1) as main:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                    f.read()
                ))
        with open(main.log_file_path()) as f:
            self.assertTrue(re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                f.read()
            ))

        with rapydmain(fw_root_dir2) as main:
            pass
        with open(main.log_file_path()) as f:
            self.assertTrue(not re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                f.read()
            ))

        with rapydmain(fw_root_dir3) as main:
            pass
        with open(main.log_file_path()) as f:
            self.assertTrue(not re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                f.read()
            ))

        with rapydmain(fw_root_dir4) as main:
            pass
        with open(main.log_file_path()) as f:
            self.assertTrue(not re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                f.read()
            ))

    def test_init_config_property_fw_logger_output_error_message_enables(self):
        # setup
        fw_root_dir1 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_error_message_enables', 'output_error_message_enables_true')
        fw_root_dir2 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_error_message_enables', 'output_error_message_enables_false')
        fw_root_dir3 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_error_message_enables', 'output_error_message_enables_not_boolean1')
        fw_root_dir4 = Path(__file__).parent / Path('test_init_config_property', 'fw_logger_output_error_message_enables', 'output_error_message_enables_not_boolean2')
        self._clean_dirs([
            fw_root_dir1 / Path('log'),
            fw_root_dir2 / Path('log'),
            fw_root_dir3 / Path('log'),
            fw_root_dir4 / Path('log')
        ])

        # test
        try:
            with rapydmain(fw_root_dir1) as main:
                with open(main.log_file_path()) as f:
                    self.assertTrue(not re.search(
                        r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                        f.read()
                    ))
                raise Exception('any')
        except:
            with open(main.log_file_path()) as f:
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                    f.read()
                ))

        try:
            with rapydmain(fw_root_dir2) as main:
                with open(main.log_file_path()) as f:
                    self.assertTrue(not re.search(
                        r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                        f.read()
                    ))
            raise Exception('any')
        except:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                    f.read()
                ))

        try:
            with rapydmain(fw_root_dir3) as main:
                with open(main.log_file_path()) as f:
                    self.assertTrue(not re.search(
                        r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                        f.read()
                    ))
            raise Exception('any')
        except:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                    f.read()
                ))

        try:
            with rapydmain(fw_root_dir4) as main:
                with open(main.log_file_path()) as f:
                    self.assertTrue(not re.search(
                        r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                        f.read()
                    ))
            raise Exception('any')
        except:
            with open(main.log_file_path()) as f:
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                    f.read()
                ))

    def test_init_config_property_fw_message(self):
        # setup
        fw_root_dir1 = Path(__file__).parent / Path('test_init_config_property', 'fw_message', 'message1')
        fw_root_dir2 = Path(__file__).parent / Path('test_init_config_property', 'fw_message', 'message2')
        fw_root_dir3 = Path(__file__).parent / Path('test_init_config_property', 'fw_message', 'message_empty1')
        fw_root_dir4 = Path(__file__).parent / Path('test_init_config_property', 'fw_message', 'message_empty2')
        self._clean_dirs([
            fw_root_dir1 / Path('log'),
            fw_root_dir2 / Path('log'),
            fw_root_dir3 / Path('log'),
            fw_root_dir4 / Path('log')
        ])

        # test
        with rapydmain(fw_root_dir1) as main:
            with open(main.log_file_path()) as f:
                log_value = f.read()
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                    log_value
                ))
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                    log_value
                ))
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                    log_value
                ))
        with open(main.log_file_path()) as f:
            self.assertTrue(re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: end\.',
                f.read()
            ))

        try:
            with rapydmain(fw_root_dir2) as main:
                raise Exception('any')
        except Exception:
            pass
        with open(main.log_file_path()) as f:
            log_value = f.read()
            self.assertTrue(re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: begin\.',
                log_value
            ))
            self.assertTrue(re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: error\.',
                log_value
            ))

        with rapydmain(fw_root_dir3) as main:
            with open(main.log_file_path()) as f:
                log_value = f.read()
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: \s',
                    log_value
                ))
                self.assertTrue(not re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: \s',
                    log_value
                ))
        with open(main.log_file_path()) as f:
            self.assertTrue(re.search(
                r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: $',
                f.read()
            ))

        try:
            with rapydmain(fw_root_dir4) as main:
                raise Exception('any')
        except Exception:
            with open(main.log_file_path()) as f:
                log_value = f.read()
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[INFO\]: \s',
                    log_value
                ))
                self.assertTrue(re.search(
                    r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\[ERROR\]: \s',
                    log_value
                ))

    def test_init_config_property_any(self):
        with rapydmain(Path(__file__).parent / Path('test_init_config_property', 'any', 'any_property')) as main:
            # config level1
            self.assertEqual(main.config['test1']['test_section1']['key1'], 'value1-1-1')
            self.assertEqual(main.config['test1']['test_section1']['key2'], 'value1-1-2')
            self.assertEqual(main.config['test1']['test_section2']['key1'], 'value1-2-1')
            self.assertEqual(main.config['test1']['test_section2']['key2'], 'value1-2-2')

            # config level2
            self.assertEqual(main.config['testdir1/test2']['test_section1']['key1'], 'value1-2-1-1')
            self.assertEqual(main.config['testdir1/test2']['test_section1']['key2'], 'value1-2-1-2')
            self.assertEqual(main.config['testdir1/test2']['test_section2']['key1'], 'value1-2-2-1')
            self.assertEqual(main.config['testdir1/test2']['test_section2']['key2'], 'value1-2-2-2')

            # not load .json config
            self.assertTrue('non_json' not in main.config)

    def test_eval_bool(self):
        self.assertTrue(rapydmain.eval_bool(True))
        self.assertFalse(rapydmain.eval_bool(False))
        self.assertFalse(rapydmain.eval_bool('True'))
        self.assertFalse(rapydmain.eval_bool('False'))
        self.assertFalse(rapydmain.eval_bool(''))
        self.assertFalse(rapydmain.eval_bool('1'))
        self.assertFalse(rapydmain.eval_bool('0'))
        self.assertFalse(rapydmain.eval_bool(1))
        self.assertFalse(rapydmain.eval_bool(0))

    def test_log_file_path(self):
        # setup
        fw_root_dir1 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_1')
        fw_root_dir2 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_2')
        fw_root_dir3 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_3')
        fw_root_dir4 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_4')
        fw_root_dir5 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_5')
        fw_root_dir6 = Path(__file__).parent / Path('test_log_file_path', 'log_file_path_6')
        self._clean_dirs([
            fw_root_dir1 / Path('log'),
            fw_root_dir2 / Path('log'),
            fw_root_dir3 / Path('log'),
            fw_root_dir4 / Path('log'),
            fw_root_dir5 / Path('log'),
            fw_root_dir6 / Path('log')
        ])

        with rapydmain(fw_root_dir1) as main:
            self.assertTrue(re.search(
                r'rapydmain_\d{8}\.log$',
                str(main.log_file_path())
            ))
        with rapydmain(fw_root_dir2) as main:
            self.assertTrue(re.search(
                r'rapydMain_\d{8}\.log$',
                str(main.log_file_path())
            ))
        with rapydmain(fw_root_dir3) as main:
            self.assertTrue(re.search(
                r'RapydMain_\d{8}\.log$',
                str(main.log_file_path())
            ))
        with rapydmain(fw_root_dir4) as main:
            self.assertTrue(re.search(
                r'Rapyd_Main_\d{8}\.log$',
                str(main.log_file_path())
            ))
        with rapydmain(fw_root_dir5) as main:
            self.assertTrue(re.search(
                r'Rapyd_Main_\d{8}\.log$',
                str(main.log_file_path())
            ))
        with rapydmain(fw_root_dir6) as main:
            self.assertTrue(re.search(
                r'Rapyd_Main_\d{8}\.log$',
                str(main.log_file_path())
            ))

    def test_logger(self):
        with rapydmain(Path(__file__).parent / Path('test_logger', 'logger_enables_true')) as main:
            self.assertTrue(type(main.logger) is Logger)
        with rapydmain(Path(__file__).parent / Path('test_logger', 'logger_enables_false')) as main:
            self.assertTrue(main.logger is None)

if __name__ == "__main__":
    unittest.main()
