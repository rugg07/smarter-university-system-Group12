import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        #Clearing data if any present
        self.ctrl.clear_data()
        #Adding a quiz using add quiz method
        #Passing None as text which causes TypeError in line 63 of quizzer_controller.py
        #TypeError is cause by adding None and a string value
        quizId = self.ctrl.add_quiz(None, "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")
        questionID  = self.ctrl.get_quiz_by_id(quizId)
        self.assertIsNotNone(questionID,"The quiz can be retrieved")
        
    def test_expose_failure_02(self):
        #Setting fileName as None 
        #Creating a new QuizzesController object with filename as none
        #As soon as the object is create __init__() of quizzes_controller.py is called
        #This method inturn calls _load_data() which is used for loading data present in file
        #_load_data() makes a call to load_data() method of data_loader.py module
        #As file Name is None Type Error is caused in line 9 of data_loader.py module where os.path.join() is used to get path of the file
        #This error is popped up to line 27 of quizzes_controller.py which in turns pops up to line 19 of quizzes_controller.py
        fileName=None
        self.ctrl = QuizzesController(fileName)
        self.ctrl.clear_data()
        quizId = self.ctrl.add_quiz("q", "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes= self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes),1,"Quiz is generated as expected")

    def test_expose_failure_03(self):
        title='\ud861\udd37'
        #Clearing data if any present
        self.ctrl.clear_data()
        #Adding a quiz using add quiz method
        #Then Adding a question to the quiz using the quiz_id
        #While adding the question I am passing title as a string which cannot be encoded by UTF-8
        #Due to this UnicodeEncodeError is thrown by line 11 of utils.py which is popped up to line 78 of quizzes_controller.py
        quizId = self.ctrl.add_quiz("Quiz1", "This is a test quiz", "2023-11-07", "2023-11-14")
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")
        questionID = self.ctrl.add_question(quizId,title,"Question1")
        self.assertIsNotNone(questionID,"The quiz can be retrieved")
        

if __name__ == '__main__':
    unittest.main()