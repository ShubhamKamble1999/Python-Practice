
class List_action():
    '''
    Class for list action
    '''
    def __init__(self,numeric_list,list_len,str_list,search_variable,replaced_element,to_replace) -> None:
        self.numeric_list = numeric_list
        self.str_list = str_list
        self.list_len = list_len
        self.search_variable = search_variable
        self.replaced_element = replaced_element
        self.to_replace = to_replace

    def print_hello_message(self):
        '''
        Print hello message
        '''
        return "Hello from shubham"

    def make_list_reverse(self):
        '''
        To make string reverse
        '''
        empty_list = []
        while self.list_len >= 0:
            flag = self.numeric_list[self.list_len]
            empty_list.append(flag)
            self.list_len -= 1
        return(empty_list)

    def max_value_in_list(self):
        '''
        To find maximum value from list
        '''
        temp_max_value = 0
        for i in self.numeric_list:
            if i > temp_max_value:
                temp_max_value = i
        return(temp_max_value)

    def find_empty_string_from_list(self):
        '''
        To find empty string from list and remove it
        '''
        for i in self.str_list:
            if len(i) == 0:
                self.str_list.remove(i)
        return(self.str_list)

    def add_element_after_variable(self):
        '''
        To find the element and add element after it
        '''
        for i in range(0 ,len(self.str_list)):
            if self.str_list[i] == self.search_variable:
                loc = i + 1
                self.str_list.insert(loc , "kamble")

        return(self.str_list)

    def find_string_in_list_and_replace(self):
        '''
        To find empty string from list and remove it
        '''
        for i in range(0 ,len(self.str_list)):
            if self.str_list[i] == self.to_replace:
                self.str_list[i] = self.replaced_element
        return(self.str_list)
    
    def find_prime(self):
        '''
        To find the prime number from list
        '''
        return_list = []
        numeric_list = self.numeric_list
        for i in numeric_list:
            if i > 1:
                if i == 2:
                    return_list.append(i)
                if i%2 != 0 and i%3 != 0:
                    return_list.append(i) 
        return(return_list)