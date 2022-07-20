
# List_One = []
# List_Two = []
# count = int(input("Enter Number of numbers for the list: "))
# while count > 0 :
#     for i in range(count):
#         Public = int(input("Enter List of Number: "))
#         if Public %2 == 0:
#             List_One.append(Public)
#         elif Public %2 != 0:
#             List_Two.append(Public)
#         count -=1 
#===================================================================
# def even_odd(List:list) -> list:
#     even_number = []
#     odd_number  = []
#     for number in List :
#         if number %2 == 0:
#             even_number.append(number)
            
#         elif number %2 !=0:
#             odd_number.append(number)
#     print(f"even number{even_number}")
#     print(f"odd number{odd_number}")
#=====================================================================
def even_odd(List:list)->list:
    even_number,odd_number = [],[]
    [even_number.append(number) if number %2 == 0 else odd_number.append(number) for number in List] 
    print(f"{even_number}\n{odd_number}")
List = [1,2,3,4,5,6,7,8,9,10]  
even_odd(List)

