from django.urls import path
from . import views

urlpatterns = [
    path('', views.findView.as_view(), name='find-ride'),
    # path('', views.findRide, name='find-ride'),
    path('sortByPrice', views.priceView.as_view(), name='sortByPrice'),
    path('sortByDate', views.dateView.as_view(), name='sortByDate'),
    path('search', views.searchView.as_view(), name='search')
]
#    public static List<String> strangeSort(List<Integer> mapping, List<String> nums) {
    
#     int mapped[]=new int[10]; 
#     for(int i=0;i<10;i++){
#     mapped[mapping.get(i)]=i; 
#     }
# 	int sorter[]=new int[nums.size()]; 
#  	for(int i=0;i<nums.size();i++){
# 	String s="";
# 	for(int j=0;j<nums.get(i).length();j++)
# 		s+=mapped[(int)nums.get(i).charAt(j)-48];
# 	sorter[i]=Integer.parseInt(s);
# 	}

# 	for(int i=0;i<nums.size()-1;i++){
# 		for(int j=0;j<nums.size()-i-1;j++){
# 	if(sorter[j]>sorter[j+1]){
# 	    int temp=sorter[j];
# 	    sorter[j]=sorter[j+1];
# 	    sorter[j+1]=temp;
# 	    String temp1=nums.get(j);
# 	    nums.set(j, nums.get(j+1));
# 	    nums.set(j+1,temp1);
# 			}	
# 		}
# 	}
# 	return nums; 

# }