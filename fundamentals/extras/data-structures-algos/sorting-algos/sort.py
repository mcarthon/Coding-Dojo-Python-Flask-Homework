class Sort:

    def __init__(self):
        pass

    def selection_sort(self, array: list[int]) -> list[int]:
        if len(array) < 2:
            return array

        outer_marker = -1

        while outer_marker < len(array) - 1:

            outer_marker += 1
            inner_marker = outer_marker
            min_value_index = outer_marker
            minimum_value = array[outer_marker]

            while inner_marker < len(array):
                if array[inner_marker] <= minimum_value:
                    
                    # set new minimum
                    minimum_value = array[inner_marker]
                    min_value_index = inner_marker

                inner_marker += 1 

            # swap new min with outer_maker value
            temp = array[outer_marker]
            array[outer_marker] = array[min_value_index]
            array[min_value_index] = temp

        return array     

    def insertion_sort(self, array: list[int]) -> list[int]:
        
        if len(array) < 2:
            return array

        selected_index = 1
        runner_index = 0

        while selected_index < len(array):
            while runner_index < selected_index:
                if array[selected_index] < array[runner_index]:
                    temp = array[selected_index]
                    array[selected_index] = array[runner_index]
                    array[runner_index] = temp
                runner_index += 1
            selected_index +=1
            runner_index = 0
        
        return array







if __name__ == "__main__":    
    sort = Sort()
    array = [5,4,3,2,1,2,3,4,5]
    print(sort.selection_sort(array))

    array = []
    print(sort.selection_sort(array))

    array = [5]
    print(sort.selection_sort(array))

    array = [1,2,3,4,5]
    print(sort.selection_sort(array))

    array = [-5,4,3,2,-1,2,3,-4,-5]
    print(sort.selection_sort(array))

    array = [5,4,3,2,1,2,3,4,5]
    print(sort.insertion_sort(array))

    array = []
    print(sort.insertion_sort(array))

    array = [5]
    print(sort.insertion_sort(array))

    array = [1,2,3,4,5]
    print(sort.insertion_sort(array))

    array = [-5,4,3,2,-1,2,3,-4,-5]
    print(sort.insertion_sort(array))