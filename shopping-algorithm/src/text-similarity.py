import sense2vec
model = sense2vec.load()
freq, wood_glue = model['wood_glue|NOUN']
#freq
#824
freq, super_glue = model['super_glue|NOUN']
#freq
#2303
model.data.similarity(wood_glue, super_glue)
#0.8765814304351807
freq, furniture = model['furniture|NOUN']
#freq
#31845
model.data.similarity(wood_glue, furniture)
#0.5280759334564209
freq, porn = model['porn|NOUN']
model.data.similarity(wood_glue, porn)
#0.16509248316287994
model.data.similarity(wood_glue, wood_glue)
#0.9999999403953552