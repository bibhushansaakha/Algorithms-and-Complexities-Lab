import unittest 
import insertion as insertion
import selection as selection 

#Test Cases
test_cases = [
    ([5,4,3,2,1,0,9,8,7,6],[0,1,2,3,4,5,6,7,8,9]),
    ([9,8,7,6,5,4,3,2,1,0],[0,1,2,3,4,5,6,7,8,9]),
    ([2,4,6,8,0,1,3,5,7,9],[0,1,2,3,4,5,6,7,8,9]),
    ([1,5,0,2,6,8,3,4,7,9],[0,1,2,3,4,5,6,7,8,9]),
    ([9,8,7,6,1,2,3,4,5,0],[0,1,2,3,4,5,6,7,8,9])
]
class TestSortingAlgorithms(unittest.TestCase):
    def test_insertion_sort(self):
        for input_array, expected_output in test_cases:
            with self.subTest(input_array=input_array): #helps to identify which test case failed. 
                sorted_array = insertion.insertion_sort(input_array) #calling the function to be tested.
                self.assertEqual(sorted_array, expected_output)
    def test_selection_sort(self):
          for input_array, expected_output in test_cases:
            with self.subTest(input_array=input_array): #helps to indentify which test case it failed. 
                sorted_array = selection.selection_sort(input_array)    #calling the function to be tested.
                self.assertEqual(sorted_array, expected_output)
   
if __name__ == '__main__':
    unittest.main()