from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Karan",
        "date": date(2023, 7, 25),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
        Mountain Hiking: A Journey Beyond the Trails

        Imagine standing on a mountain peak, the cool breeze brushing against your face, and an endless panorama of majestic landscapes stretching beyond the horizon. Mountain hiking isn’t just an activity—it’s an experience that awakens your senses, tests your limits, and connects you to the purest form of nature.

        Every step on the trail tells a story. The crunch of leaves underfoot, the rustling of trees, and the occasional chirp of a bird remind you that you’re part of something larger. It’s not just about reaching the summit; it’s about the journey—the moments when you pause to marvel at a cascading waterfall or catch your breath as the sun sets, painting the sky in fiery hues.

        Hiking offers more than breathtaking views. It’s a retreat for the soul. With every uphill climb, you leave behind stress and distractions, gaining clarity and peace. It’s a chance to challenge yourself, both physically and mentally, as the trail winds and the altitude rises.

        But the magic of hiking lies in its simplicity. No notifications, no deadlines—just you, the trail, and the rhythm of your heartbeat. It’s a reminder that the best things in life aren’t behind screens but under the open sky.

        So, whether you’re a seasoned trekker or a curious beginner, pack your backpack, tie those boots, and step into the wild. The mountains are calling, and trust me, it’s an adventure you’ll never forget. 🌄✨
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Karan",
        "date": date(2024, 12, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
        Programming: The Art of Creating Magic

        Programming isn’t just about writing code—it’s about building dreams, solving problems, and bringing ideas to life. It’s the power to turn thoughts into tools, creativity into solutions, and innovation into reality.

        Think about it: with just a few lines of code, you can create a game that entertains millions, design an app that connects people across the globe, or automate tasks that save countless hours. Programming transforms abstract concepts into tangible outcomes, making it one of the most empowering skills of our time.

        The beauty of programming lies in its universality. Whether you're designing a website, crafting AI algorithms, or controlling a robotic arm, the principles remain the same. It’s like learning the language of the universe—one that speaks to innovation and progress.

        What makes programming truly great, though, is the community. Coders around the world share a bond, collaborating, troubleshooting, and celebrating breakthroughs together. It’s a constant cycle of learning, sharing, and growing.

        So, if you’ve ever thought about diving into programming, now’s the time. It’s not just a skill; it’s a superpower that unlocks endless possibilities. Start small, dream big, and let your code shape the future.

        Because in the world of programming, the only limit is your imagination. 🚀💻
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Karan",
        "date": date(2024, 6, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
        Nature at Its Best: A Symphony of Beauty and Wonder

        In a world brimming with screens and schedules, there lies an untouched masterpiece that captivates our souls—nature. Step outside, and you’ll discover a world where every leaf, stream, and sunrise tells a story.

        Picture this: golden rays of sunlight piercing through a dense canopy, the soft rustle of leaves serenading the breeze, and a horizon painted with hues no artist could ever replicate. Nature, in its finest form, is pure magic—a living canvas constantly evolving yet timeless in its beauty.

        It’s in the majesty of towering mountains, the serenity of calm lakes, and the resilience of wildflowers blooming against all odds that we find life’s most profound lessons. Nature doesn’t rush, yet everything gets accomplished. It reminds us to slow down, breathe, and savor the simple joys around us.

        Take a moment to immerse yourself. Feel the earth beneath your feet, hear the symphony of chirping birds, and watch the dance of clouds above. Nature’s rhythm has a way of healing, inspiring, and grounding us like nothing else.

        So, unplug for a while and step into the wild. In the embrace of nature, you’ll not only witness its best but also rediscover the best in yourself. 🌿✨
        """
    }
]

# Create your views here.

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts' : latest_posts,
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts,
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug) #returns the post when slug value matches the actual slug
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
    })
