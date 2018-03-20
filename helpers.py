import json

# def hashtagacquire():
#     error=None
#     if form.find('#')==-1:
#         return request.form("searchbox")
#     else:
#         error = ('Input must include #')

def fallback_to_file(file_name):
    with open(file_name, "r") as f:
        res = json.load(f)
    return res

def hashtagcheck(searchterm):
    #form=input("choose hashtag...")
    form=searchterm
    if form.find('#')==-1:
        print("Error")
        print("Please include a hashtag symbol.")
    # else
    #     print(searchterm)

# function myFunction(){
#     document.getElementById("Dropsearch").classList.toggle("show");}
#
# function filterFunction(){
#     var input, filter, ul, li, a, i;
#     input = document.getElementById("myInput");
#     filter = input.value.toUpperCase();
#     div = document.getElementById("Dropsearch");
#     a = div.getElementsByTagName("a");
#     for (i = 0; i < a.length; i++) {
#         if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
#             a[i].style.display = "";
#         } else {
#             a[i].style.display = "none";
#         }
#     }
# }
