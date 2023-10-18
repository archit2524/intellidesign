
#TODO-- dalle module
import openai

openai.api_key = "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" #TODO-- API key

model = "image-alpha-001"

def main(get_prompt):

    prompt=get_prompt #TODO-- To get user enterd prompt
    complete = openai.Image.create(prompt=prompt,n=1) #TODO-- it creates  the image 
    print(complete)
    mainurl=complete["data"][0]["url"]#TODO-- it returns original url from the generated dictionary 
    print(mainurl)

    return mainurl

# def variation():
#     v_response = openai.Image.create_variation(
#     image=open("room3.png", "rb"),

#     n=1,
    # )
    # v_url=v_response["data"][0]["url"]
    # print(v_url)
    # webbrowser.open(v_url)
# variation()



