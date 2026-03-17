

class BinarySearch:

    def solution(self,arr:list,element:int):


        low = 0

        upp=len(arr)-1

        is_present=False


        while(low <=upp):

            mid=(low+upp)//2


            if (element==arr[mid]):

                is_present=True

            elif (element < arr[mid]):

                upp=mid -1

            elif element(element > arr[mid]):

                low = mid +1


            return is_present

bs_instance=BinarySearch()

arr=[10,11,12,13,14]

element=int(input("enter the element"))

print(bs_instance.solution(arr,element))





            

            
                

               










        



        