from transformers import pipeline

model = pipeline('sentiment-analysis')

print(model("Hello.")[0]['label'])
print(model("I hate you.")[0]['label'])
print("{:.2f}".format(model("12345")[0]['score'] * 100))


