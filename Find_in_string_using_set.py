import random
import time
start = time.time()

txt ="The United States and the Soviet Union emerged as rival superpowers in the aftermath of World War II. During the Cold War, the two countries confronted each other indirectly in the arms race, the Space Race, propaganda campaigns, and localized wars against communist expansion. In the 1960s, in large part due to the strength of the civil rights movement, another wave of social reforms was enacted which enforced the constitutional rights of voting and freedom of movement to African Americans. The Cold War ended when the Soviet Union was officially dissolved, leaving the United States as the world's sole superpower. Foreign policy after the Cold War has often focused on many modern conflicts in the Middle East, especially in response to the September 11 attacks. Early in the 21st century, the United States experienced the Great Recession and the COVID-19 pandemic, which had a negative effect on the local economy. Encouraged by the notion of manifest destiny, the United States expanded to the Pacific Coast. While the nation was large in terms of area, its population in 1790 was only four million. Westward expansion was driven by a quest for inexpensive land for yeoman farmers and slave owners. The expansion of slavery was increasingly controversial and fueled political and constitutional battles, which were resolved by compromises. Slavery was abolished in all states north of the Mason–Dixon line by 1804, but states in the south continued the institution, to support the kinds of large scale agriculture that dominated the southern economy. The division of the country along these lines formed the major political issue of the first eight decades of the growth of the United States. Precipitated by the election of Abraham Lincoln as president in 1860, the Civil War began as the southern states seceded from the Union to form their own pro-slavery country, the Confederate States of America. The defeat of the Confederates in 1865 led to the abolition of slavery. In the Reconstruction era following the war, legal and voting rights were extended to freed slaves. The national government emerged much stronger, and gained explicit duty to protect individual rights. However, when white southern Democrats regained their political power in the South in 1877, often by paramilitary suppression of voting, they passed Jim Crow laws to maintain white supremacy, as well as new state constitutions that legalized discrimination based on race and prevented most African Americans from participating in public life."
thisset = set()
word = ""

for x in range(0,len(txt)):
    letter=txt[x]
    if letter==" ":
        thisset.add(word)
        word = ""
    else:
        word += letter

for i in range(1000000):
     temp = random.randint(0, 1)
     #print(temp)
     if temp == 1:
       y = "public"
     else:
       y = ""
     print(y in thisset)



end = time.time()
print(end - start)
