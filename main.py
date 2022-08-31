from os import lseek
from list_action.list_action import List_action
from constants.common import *
from tuple_action.tuple_action import Tuple_action
from print import print_values
numeric_list = NUMERIC_LIST
str_list = STR_LIST
replaced_element = REPLACE_WITH
to_replace = TO_REPLACE 
numeric_tuple = NUMERIC_TUPLE
string_tuple = SRTING_TUPLE
tuple1 = TUPLE1
tuple2 = TUPLE2

list_len = len(numeric_list) -1
tuple_len = len(numeric_tuple) -1

search_variable = SEARCH_VARIABLE

list_object = List_action(numeric_list=numeric_list,list_len=list_len ,str_list=str_list , search_variable=search_variable,replaced_element=replaced_element,to_replace=to_replace)
print(list_object.print_hello_message())
rev_list = list_object.make_list_reverse()
max_value = list_object.max_value_in_list()
empty_string = list_object.find_empty_string_from_list()
append_element = list_object.add_element_after_variable()
replace_element = list_object.find_string_in_list_and_replace()
find_prime = list_object.find_prime()

output = print_values.print_list_output(rev_list=rev_list,max_value=max_value,empty_string=empty_string,append_element=append_element,replace_element=replace_element,find_prime=find_prime)
print("Output",output)

tuple_object = Tuple_action(numeric_tuple=numeric_tuple,string_tuple=string_tuple,tuple_len=tuple_len,tuple1=tuple1,tuple2=tuple2)

reverse_tuple = tuple_object.reverse_tuple()
swap_tuple = tuple_object.swap_tuple()
# print_values(reverse_tuple=reverse_tuple ,swap_tuple=swap_tuple)
# print("swap_tuple ->",swap_tuple)
