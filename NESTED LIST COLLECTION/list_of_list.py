social_media_post=[

    [1,"good morning",500,600,"Rahul"],
  
    [2,"good aftrnun",400,700,"Vipin"],
    
    [3,"hai",600,800,"Raj"],

    [4,"helloo all" ,450,300,"Akash"],
    [5,"helloo all" ,450,500,"Adhil"]

]

print(social_media_post[1][2])

print(social_media_post[0][4])

fb_views=[fv[2] for fv in social_media_post]

print(f"Facebook views {fb_views}")

insta_views=[iv[3] for iv in social_media_post]

print(f"Instagram views {insta_views}" )

facebok_views=[lst[4] for lst in social_media_post if lst[3]==500]

print(facebok_views)


max_insta_views=max([lst[-2] for lst in social_media_post ])

max_insta_views=[lst[-1] for lst in social_media_post if lst[-2]==max_insta_views]

print(max_insta_views)


min_insta_views=min([lst[-2] for lst in social_media_post])
min_insta_views=[lst[-1] for lst in social_media_post if lst[-2]==min_insta_views]
print(min_insta_views)
