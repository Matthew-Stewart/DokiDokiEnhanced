define urname = 'You'

image bg classroom = "classroom.jpg"
image bg hallway = "hallway.jpg"

image sy-joy = im.FactorScale("sayako-joy.png", 0.8)
image sy-ang = im.FactorScale("sayako-angry.png", 0.8)
image sy-ann = im.FactorScale("sayako-annoyed.png", 0.8)

image ms-joy = im.FactorScale("mitsuki-joy.png", 0.15)
image ms-ang = im.FactorScale("mitsuki-angry.png", 0.8)
image ms-con = im.FactorScale("mitsuki-concerned.png", 0.8)
image ms-neu = im.FactorScale("mitsuki-neutral.png", 0.8)
image ms-sup = im.FactorScale("mitsuki-surprised.png", 0.8)

# Declare characters used by this game.
define n  = Character('' , color ="#36d1cb")
define mc = Character("[urname]", color="#c8ffc8")
define ms = Character("Mitsuki", color="#efa21c")
define l = Character("???", color="#e03cdd")
define s = Character("Sayako", color="#f72525")


define temp =""
define broad = False


# The game starts here.
label start:

    scene bg classroom
    with dissolve
    
    play music "Rainbows.mp3"
    
    $ urname =renpy.input("What is your name?") or "Dat Boi"
    
    n "You’re in a classroom and the bell is about to ring. You’re anxious and really want to leave."
    n "Bell rings."
    
    l "[urname]-chan! Wait Up!"

    n "It's Mitsuki, your best friend since grade school."

    n  "Mitsuki runs up to greet you."
    
    show ms-joy
    ms "[urname]! How are you?"
    
    mc "{color=#ceccc6}{i}There’s that radiant smile of hers. She always seems to be in a good mood when I see her at school.{/i}{/color}"
    menu:
        "I'm good!":
            
            python:
               import response
               temp = response.Reaction().get_mood()
               
            if temp == "anger" or temp == "sorrow":
               show ms-con
               ms "Really? You don’t look so good."
               mc "{color=#ceccc6}{i}There she goes again reading me like a book. Being friends with her for so long she can tell something’s wrong.{/i}{/color}"
               jump first
            elif temp == "joy":
               show ms-joy
               ms "That’s great to hear! When you’re happy, I’m happy!"
               jump second
            elif temp == "surprise":
               show ms-sup
               ms "Tell me about it. You look like you’ve seen a ghost."
               jump first
            else:
               show ms-joy
               ms "That’s great to hear! When you’re happy, I’m happy!"
               jump second
            
        "I've been better.":
        
            python:
               import response
               temp = response.Reaction().get_mood()
               
            if temp == "sorrow":
               show ms-con
               
               ms "What’s the matter? You seem upset."
               mc "{color=#ceccc6}{i}It’s nice to have a friend like her. She gets really concerned when she senses something wrong with one of her friends.{/i}{/color}"
               
               jump first
               
            elif temp =="anger":
               show ms-sup
               
               ms "Whoa, chill out! What’s wrong?"
               jump first
               
            elif temp == "joy":
               show ms-joy
               
               ms "Too real."
               mc "{color=#ceccc6}{i}She can relate with me. Sometimes things aren’t going well, but we have to try to keep our positivity. {/i}{/color}"
              
               jump second
               
            elif temp == "surprise":
               show ms-con
               
               ms "Tell me about it. You look like you’ve seen a ghost."
               jump first
               
            else:
               show ms-joy
               ms "Too real."
               jump second
        
    label first:
    
       menu:
           "I'm fine!":
              jump third
           "You know that one girl that always sits next to me?":
              jump fourth
    
    label second:
       mc "Well..."
       mc "You know that one girl that always sits next to me?"
       jump fourth
    
    label third:
       python:
          import response
          temp = response.Reaction().get_mood()
       
       if temp == "joy":
          show ms-ang
          
          ms "You’re a terrible liar. What’s really going on?"
          mc "{color=#ceccc6}{i}She saw through me immediately...{/i}{/color}"
          mc "You know that one girl that always sits next to me?"
          
       elif temp == "anger" or temp == "surprise":
          show ms-ang
          
          ms "Man, what is up with you?"
          mc "{color=#ceccc6}{i}Uh oh… I don’t usually see Mitsuki like this.{/i}{/color}"
          mc "You know that one girl that always sits next to me?"
       
       elif temp == "sorrow":
          show ms-con
          
          ms "Hey, cheer up! I’m sure you’ll get through this… You sure you don’t want to talk about it?"
          mc "{color=#ceccc6}{i}Mitsuki somehow manages to always lift my spirits when I’m down...{/i}{/color}"
          mc "You know that one girl that always sits next to me?"
          
       else:
          show ms-ang
          
          ms "You’re a terrible liar. What’s really going on?"
          mc "{color=#ceccc6}{i}She saw through me immediately...{/i}{/color}"
          mc "You know that one girl that always sits next to me?"

    label fourth:
       ms "You mean Sayako? Yeah, I do. Why?"
       menu:
          "She's a total broad.":
             $ broad = True
             ms "What’d she do this time?"
             mc "She tried to cheat off my quiz."
          "She tried to cheat off my quiz.":
             jump fifth
                 
    label fifth:
       show ms-ang
       ms "That's horrible! But I'm not surprised."
       menu:
          "Yeah... I should talk to her.":
             jump sixth
          "it's fine, I didn't do that well anyway.":
             jump seventh
    label sixth:
        python:
          import response
          temp = response.Reaction().get_mood()
    
    if temp == "joy":
        show ms-ang
        
        ms "Why do I get the feeling you’re about to say something stupid to her?"
        mc "Too late. She’ll get what’s coming to her"

        hide ms-ang
        jump eighth
    elif temp == "anger":
        show ms-con
        
        ms "I think you should take some time to clear your head first."
        mc "Yeah, you're probably right."
        
        hide ms-con
        hide ms-ang
        hide ms-neu
        jump ninth
    elif temp == "sorrow":
        show ms-con
        
        ms "You sure? You don’t look so good."
        mc "Yeah, I’m gonna go home."
        
        hide ms-con
        jump ninth                       
    elif temp == "surprise":
        show ms-neu
       
        ms "Yeah… you should."
        mc "I have a bad feeling bad about this..."
       
        hide ms-neu
        jump eighth
        
    else:
        show ms-ang
        
        ms "Why do I get the feeling you’re about to say something stupid to her?"
        mc "Too late. She’ll get what’s coming to her"
        
        hide ms-ang
        jump eighth
        
    label seventh:
    
        python:
           import response
           temp = response.Reaction().get_mood()
           
        if temp == "joy":
           show ms-joy
           
           ms "You're such a jerk lmao."
           mc "I know. ;)"
           
           hide ms-joy
           jump eighth
           
        else:
           show ms-joy
          
           ms "You don’t need to be that hard on yourself. I’m sure you did fine."
           mc "Yeah, I’m fine. {i}Everything’s fine.{/i}"
          
           hide ms-joy
           jump ninth
    
    # Part 2          
           
    label eighth:
    
       scene bg hallway
       with dissolve
       
       play music "Clash_Defiant.mp3"
       
       l "Hey, watch where you're going, jerk!"
       
       n "You bump into Sayako, standing outside the door."
      
       show sy-ang
       hide ms-ang
       hide ms-neu
       hide ms-con

       menu:
             "Oh, hey Sayako! I'm really sorry!":
                jump tenth
             "Wait... were... you spying on me? O_o":
                jump eleventh
                
    label ninth:
       scene bg hallway
       with dissolve

       play music "Clash_Defiant.mp3"

       n "You start walking down the hallway when you hear Sayako."
       
       show sy-ang
       hide ms-ang

       
       if broad == True:
          show ms-ang
          s "So, you think I’m a broad, huh?" 
          menu:
             "Oh... uh...":
                jump twelfth
             "Yeah...":
                jump thirteenth
       else:
          show ms-ang
          s "You have something you want to say to me?" 
          menu:
             "Hi Sayako!":
                jump twelfth
             "Yeah I do.":
                jump thirteenth    
          
    label tenth:
       
       if broad == True:
          show sy-ang
          s "So, you think I'm a broad, huh?"
          s " Save the goodie two shoes act. I heard you talking about me in there."
       else:
          show sy-ann
          s " Save the goodie two shoes act. I heard you talking about me in there."
       
       menu:
       
          "Yeah, I know you cheated off of my test. And if you do it again, you’ll regret it. Don’t try me.":
             mc "{color=#ceccc6}{i}If the faculty knows about this, she’ll easily get expelled{/i}{/color}."
             jump blackmail
          "Yeah, we were talking about how great you are!":
             jump romance
             
    label eleventh:
    
       if broad == True:
          show sy-ang
          s "So, you think I'm a broad, huh?"
          s "And no, I just happened to be standing here."
       else: 
          show sy-ann
          s "And no, I just happened to be standing here."

       mc "{color=#ceccc6}{i}Oh, I’m in real deep.{/i}{/color}"
       menu:
          "Sure you were. And I’m the queen of England. Look, if you try to cheat off of me again, you’ll regret it.":
             mc "{color=#ceccc6}{i}If the faculty knows about this, she’ll easily get expelled{/i}{/color}."
             jump blackmail
          "That's a lie and you know it.":
             jump ydfu
             
    label twelfth:
       show sy-ann
       s "Save the goodie two shoes act. I heard you talking about me in there."
    
    menu:
       "Err… we were just talking about how amazing you are!":
          jump blackmail
       "Yeah. What’re you gonna do about it?":
          jump ydfu
   
    label thirteenth:
    
    show sy-ang
    
    s "So? Spill it!" 
    
    mc "I… I just want to say… how I truly feel about you… is that..."
    
    menu:
       "You’re the most beautiful girl I’ve ever met.":
          mc "{color=#ceccc6}{i}Holyshitholyshitholyshit what are you thinking?!{/i}{/color}"
          jump romance
       "You’re a horrible person. Stop cheating off of me.":
          jump ydfu
    
    label ydfu:
       show sy-ang
       n "She slaps you"
       python:
          import response
          temp = response.Reaction().get_mood() 
          
       if(temp == "anger" and temp == "suprise"):
          s "You definitely deserved that."
       elif temp == "sorrow":
          s "Quite crying, you baby..."
       else:
          s "You sadistic moron..."
       jump end
       
    label blackmail:
       show sy-ann
       python:
          import response
          temp = response.Reaction().get_mood()
          
       if(temp == "anger" and temp == "suprise"):
          s "Wipe that smug look off your face!"
       elif temp == "sorrow":
          s "Yeesh, okay! It won’t happen again."
       else:
          s "Alright, fine. I guess you do actually care. I won’t do it again."
       jump end
    
    label romance:
       play music "Cheery_Monday.mp3"
       show sy-joy
       n "She leans in."
       
       python:
          import response
          temp = response.Reaction().get_mood()    
          
       if temp == "anger":
          s "You look so cute when you’re angry!"
       elif temp == "surprise":
          s "What? You didn’t think I felt the same?"
       elif temp == "sorrow":
          s "It’s okay! I feel the same way about you!"
       else:
          s "I love you, [urname]-chan!"
          
    label end:
       
     return
