import json

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
    #print(searchterm)
