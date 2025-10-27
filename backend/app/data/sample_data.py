"""
Sample Data Module
Contains initial data for restaurants with complete branding
"""
from app.models import MenuItem, Menu, MenuCategory, DietaryTag, Restaurant


def create_kurdies_curry_menu() -> Menu:
    """Create menu for Kurdie's Curry"""
    menu_items = [
        # Appetizers
        MenuItem(
            id=1,
            name="Samosas",
            description="Crispy pastry filled with spiced potatoes and peas.",
            price=5.99,
            category=MenuCategory.APPETIZERS,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuC9ypkMSdD7USA7GCgtYuS1pjmY3R3GZaH9CJV_JiArzroBekQEiJj7Vim4j1JsYlj6j4VvWm6CE5DfVuyy5IO6WELXDXH-YDDZeg3FMmeZkDIhX7pWksHZ8LVf_KYRgOsjaYwAgSjRSIQgVdLkUkzo9KNrB4b7wvpFyme1GSYVbs7DMPK76sUo7JztvBUvzdCwDBAy88oOkmKT_-2DOxdEsF32Qo6fs0cS6i5dCj5l1WTI9e12jy3aeebNepNidW2m5sTzA1at9wOr"
        ),
        MenuItem(
            id=2,
            name="Pakoras",
            description="Mixed vegetables fried in a spiced chickpea batter.",
            price=6.99,
            category=MenuCategory.APPETIZERS,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDIQcw3pXXpizzeOmkps2oSbVSWzliwqabmGyZkxSroAs5oDt1r7sPtm8YQMHqR-HSHgPNwEP2X9tWn_TcejCmLLxnQuYtugkePNR2AINp9vJ0cX-d-Opahf52Oev5HJBVp6_iabXs6Z9UMA28uOEVuPq8ZUsHKQ7OM9sMyJiMx2AGQhxzIRQheeci3sgNm00-YpdT-xel4CNdjR18wOqPf7F_iUb3FhUotIgBuS2x_GcCyREZs-lMhA8Bsoypux6DjiE6Vk7UCNyqU"
        ),
        MenuItem(
            id=3,
            name="Onion Bhaji",
            description="Crispy fried onion fritters with aromatic spices.",
            price=5.49,
            category=MenuCategory.APPETIZERS,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.VEGAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuC9ypkMSdD7USA7GCgtYuS1pjmY3R3GZaH9CJV_JiArzroBekQEiJj7Vim4j1JsYlj6j4VvWm6CE5DfVuyy5IO6WELXDXH-YDDZeg3FMmeZkDIhX7pWksHZ8LVf_KYRgOsjaYwAgSjRSIQgVdLkUkzo9KNrB4b7wvpFyme1GSYVbs7DMPK76sUo7JztvBUvzdCwDBAy88oOkmKT_-2DOxdEsF32Qo6fs0cS6i5dCj5l1WTI9e12jy3aeebNepNidW2m5sTzA1at9wOr"
        ),
        # Signature Dishes
        MenuItem(
            id=4,
            name="Butter Chicken",
            description="Tender chicken in a creamy tomato sauce.",
            price=15.99,
            category=MenuCategory.SIGNATURE_DISHES,
            tags=[],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDr4N94yuEhj8qNNsrRbly228PUanmCqLnXylSS0F_V5lkGtiPY3wWy-4c-7D9l6wVJbHdpabgmwWSXqbxJ5r59QvMfLFDN8wLGoB11HseUbUwTdzSlxI_61xlDGWXjYaHXWpYBhfTpnF8HXhFAVULOnoFWYLGX9I93kV7AfvVo3hXVebLE9HUTmjCh511JSlAssyBe-WNDjQLCDUCFVAkWcupJEEPa_ig8NnD2uTwBJyltDHOfS7hROqSX831RrSZMcARmMYtt4-k2"
        ),
        MenuItem(
            id=5,
            name="Chana Masala",
            description="Chickpeas cooked in a tangy onion and tomato gravy.",
            price=13.99,
            category=MenuCategory.SIGNATURE_DISHES,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.VEGAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuA0DftJlZkTTtvnMukAfyrVoTLaHAWBjQxYA8NXsjUy-1m_P-IW-F7A8vlxawXjpGNR2DjxZpf8cWhEkmLBhuirSENesWipXvkLLyM2K6qev_TKnVytDLX-EyvJPb3W-7ax6-hpfvyRUxSdJASZbZP4MoH-nwZCoE33ap9R13AVlu96DaRuXwIhYqaSBKY7gZhXgMJQtv7Dvn6xVplWz1T9xu5-F2qpw6aXPqG65Orfywyxo7ie0CGC9lKG07R-jhBidkGYfz5i7jkc"
        ),
        MenuItem(
            id=6,
            name="Lamb Rogan Josh",
            description="Aromatic lamb curry with Kashmiri spices.",
            price=17.99,
            category=MenuCategory.SIGNATURE_DISHES,
            tags=[DietaryTag.GLUTEN_FREE, DietaryTag.DAIRY_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDr4N94yuEhj8qNNsrRbly228PUanmCqLnXylSS0F_V5lkGtiPY3wWy-4c-7D9l6wVJbHdpabgmwWSXqbxJ5r59QvMfLFDN8wLGoB11HseUbUwTdzSlxI_61xlDGWXjYaHXWpYBhfTpnF8HXhFAVULOnoFWYLGX9I93kV7AfvVo3hXVebLE9HUTmjCh511JSlAssyBe-WNDjQLCDUCFVAkWcupJEEPa_ig8NnD2uTwBJyltDHOfS7hROqSX831RrSZMcARmMYtt4-k2"
        ),
        MenuItem(
            id=7,
            name="Palak Paneer",
            description="Soft cottage cheese in creamy spinach curry.",
            price=14.99,
            category=MenuCategory.SIGNATURE_DISHES,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuA0DftJlZkTTtvnMukAfyrVoTLaHAWBjQxYA8NXsjUy-1m_P-IW-F7A8vlxawXjpGNR2DjxZpf8cWhEkmLBhuirSENesWipXvkLLyM2K6qev_TKnVytDLX-EyvJPb3W-7ax6-hpfvyRUxSdJASZbZP4MoH-nwZCoE33ap9R13AVlu96DaRuXwIhYqaSBKY7gZhXgMJQtv7Dvn6xVplWz1T9xu5-F2qpw6aXPqG65Orfywyxo7ie0CGC9lKG07R-jhBidkGYfz5i7jkc"
        ),
        # Bread and Sides
        MenuItem(
            id=8,
            name="Garlic Naan",
            description="Soft flatbread with garlic and herbs.",
            price=3.99,
            category=MenuCategory.BREAD_AND_SIDES,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDmQDuSXFNynpoFlbBFl23X4xP2Hb8UUmHXIFvktKdLxAZciyto1lWioY71zauor5w-G9VU_mZBHdttMHSV5lzByOROGflmbbL3gO9DhdVMag-iyNBdjBR1eyvNm6MFQwR78kzG4zcn0Htbv06l2esTRDVGKt3aYBI9bpLJ9TfILd8lMUZQYSy8fgHrcT24eGzu8doau-QSGJe7tp7Z9HQyI9RujgUIYR_o2tZSGaBX0Aeev3pPBBPA4FVCTxwrDFcEtFQ64KigFVs0"
        ),
        MenuItem(
            id=9,
            name="Plain Naan",
            description="Classic Indian flatbread baked in tandoor.",
            price=2.99,
            category=MenuCategory.BREAD_AND_SIDES,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDmQDuSXFNynpoFlbBFl23X4xP2Hb8UUmHXIFvktKdLxAZciyto1lWioY71zauor5w-G9VU_mZBHdttMHSV5lzByOROGflmbbL3gO9DhdVMag-iyNBdjBR1eyvNm6MFQwR78kzG4zcn0Htbv06l2esTRDVGKt3aYBI9bpLJ9TfILd8lMUZQYSy8fgHrcT24eGzu8doau-QSGJe7tp7Z9HQyI9RujgUIYR_o2tZSGaBX0Aeev3pPBBPA4FVCTxwrDFcEtFQ64KigFVs0"
        ),
        MenuItem(
            id=10,
            name="Basmati Rice",
            description="Fragrant long-grain rice, perfectly steamed.",
            price=3.49,
            category=MenuCategory.BREAD_AND_SIDES,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.VEGAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDmQDuSXFNynpoFlbBFl23X4xP2Hb8UUmHXIFvktKdLxAZciyto1lWioY71zauor5w-G9VU_mZBHdttMHSV5lzByOROGflmbbL3gO9DhdVMag-iyNBdjBR1eyvNm6MFQwR78kzG4zcn0Htbv06l2esTRDVGKt3aYBI9bpLJ9TfILd8lMUZQYSy8fgHrcT24eGzu8doau-QSGJe7tp7Z9HQyI9RujgUIYR_o2tZSGaBX0Aeev3pPBBPA4FVCTxwrDFcEtFQ64KigFVs0"
        ),
        MenuItem(
            id=11,
            name="Raita",
            description="Cooling yogurt with cucumber and spices.",
            price=2.99,
            category=MenuCategory.BREAD_AND_SIDES,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuDmQDuSXFNynpoFlbBFl23X4xP2Hb8UUmHXIFvktKdLxAZciyto1lWioY71zauor5w-G9VU_mZBHdttMHSV5lzByOROGflmbbL3gO9DhdVMag-iyNBdjBR1eyvNm6MFQwR78kzG4zcn0Htbv06l2esTRDVGKt3aYBI9bpLJ9TfILd8lMUZQYSy8fgHrcT24eGzu8doau-QSGJe7tp7Z9HQyI9RujgUIYR_o2tZSGaBX0Aeev3pPBBPA4FVCTxwrDFcEtFQ64KigFVs0"
        ),
        # Beverages
        MenuItem(
            id=12,
            name="Mango Lassi",
            description="Yogurt-based drink with sweet mango.",
            price=4.99,
            category=MenuCategory.BEVERAGES,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCWh5zafvFj0J047RiAQXzsnGUOoEkUOGv1EDSw90xbJ4bfhQmYtDh-3ep44ZVkNEOOkVYQUDKunBnyyc5-bRp6v6XUDjEfwkzbFSj22d5NOIFTgWXftfHBZtKL63nGkmXsnDKiL8F2POhfYwSI1ELr68SsIjKxAQRBQqNi4PippU16wItMecXa5xFuNNa_ZV1uMQa4zmsBqGmNI5alu8MHltbMiQvBEMB3BEmAEalLgQDcXYLfc6V04ms7IAOHLMXKBopzmFQHkpfi"
        ),
        MenuItem(
            id=13,
            name="Chai Tea",
            description="Traditional spiced Indian tea with milk.",
            price=3.49,
            category=MenuCategory.BEVERAGES,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCWh5zafvFj0J047RiAQXzsnGUOoEkUOGv1EDSw90xbJ4bfhQmYtDh-3ep44ZVkNEOOkVYQUDKunBnyyc5-bRp6v6XUDjEfwkzbFSj22d5NOIFTgWXftfHBZtKL63nGkmXsnDKiL8F2POhfYwSI1ELr68SsIjKxAQRBQqNi4PippU16wItMecXa5xFuNNa_ZV1uMQa4zmsBqGmNI5alu8MHltbMiQvBEMB3BEmAEalLgQDcXYLfc6V04ms7IAOHLMXKBopzmFQHkpfi"
        ),
        MenuItem(
            id=14,
            name="Sweet Lassi",
            description="Traditional sweet yogurt drink.",
            price=4.49,
            category=MenuCategory.BEVERAGES,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCWh5zafvFj0J047RiAQXzsnGUOoEkUOGv1EDSw90xbJ4bfhQmYtDh-3ep44ZVkNEOOkVYQUDKunBnyyc5-bRp6v6XUDjEfwkzbFSj22d5NOIFTgWXftfHBZtKL63nGkmXsnDKiL8F2POhfYwSI1ELr68SsIjKxAQRBQqNi4PippU16wItMecXa5xFuNNa_ZV1uMQa4zmsBqGmNI5alu8MHltbMiQvBEMB3BEmAEalLgQDcXYLfc6V04ms7IAOHLMXKBopzmFQHkpfi"
        ),
        # Desserts
        MenuItem(
            id=15,
            name="Gulab Jamun",
            description="Soft, spongy balls soaked in a sweet syrup.",
            price=5.99,
            category=MenuCategory.DESSERTS,
            tags=[DietaryTag.VEGETARIAN],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCRdlshHqujWZ6CwI6wlFvxUgKdZEuK-YNqgsogRZSfrzYPJbVJLEbA3dBrg4gCJfU3xsiJGiOylkJOYih4LtNYTB0Nec8gwo3wt1IhEGAcoljBe6eib0DpQHxqGLDjK9qlpUfLT8x4SZGBFOSNReOuTXCGy8zxUU2owqXwI65sXWdFPlakFXCSmvFpsxsKSBY5QILpk5GOkTqfAsME7gibWINrPxo64etQzzJ8CF9P4Okzlpr64VjjgQFjrx5wMk8lo9BrBZ8pEECR"
        ),
        MenuItem(
            id=16,
            name="Kheer",
            description="Creamy rice pudding with cardamom and nuts.",
            price=4.99,
            category=MenuCategory.DESSERTS,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCRdlshHqujWZ6CwI6wlFvxUgKdZEuK-YNqgsogRZSfrzYPJbVJLEbA3dBrg4gCJfU3xsiJGiOylkJOYih4LtNYTB0Nec8gwo3wt1IhEGAcoljBe6eib0DpQHxqGLDjK9qlpUfLT8x4SZGBFOSNReOuTXCGy8zxUU2owqXwI65sXWdFPlakFXCSmvFpsxsKSBY5QILpk5GOkTqfAsME7gibWINrPxo64etQzzJ8CF9P4Okzlpr64VjjgQFjrx5wMk8lo9BrBZ8pEECR"
        ),
        MenuItem(
            id=17,
            name="Rasmalai",
            description="Soft cheese patties in sweet, creamy milk.",
            price=6.49,
            category=MenuCategory.DESSERTS,
            tags=[DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE],
            image="https://lh3.googleusercontent.com/aida-public/AB6AXuCRdlshHqujWZ6CwI6wlFvxUgKdZEuK-YNqgsogRZSfrzYPJbVJLEbA3dBrg4gCJfU3xsiJGiOylkJOYih4LtNYTB0Nec8gwo3wt1IhEGAcoljBe6eib0DpQHxqGLDjK9qlpUfLT8x4SZGBFOSNReOuTXCGy8zxUU2owqXwI65sXWdFPlakFXCSmvFpsxsKSBY5QILpk5GOkTqfAsME7gibWINrPxo64etQzzJ8CF9P4Okzlpr64VjjgQFjrx5wMk8lo9BrBZ8pEECR"
        ),
    ]
    
    menu = Menu()
    for item in menu_items:
        menu.add_item(item)
    
    return menu


def create_sample_restaurants():
    """
    Create sample restaurants with complete branding and information
    """
    restaurants = []
    
    # Restaurant 1: Kurdie's Curry
    kurdies_menu = create_kurdies_curry_menu()
    
    kurdies_curry = Restaurant(
        id="kurdiescurry",
        name="Kurdie's Curry",
        slug="kurdiescurry",
        tagline="Authentic Flavors, Modern Twist",
        
        # Contact
        address="1337 N Spice Rd, Prescott Valley, AZ 86314",
        phone="(928) 555-1337",
        email="info@kurdiescurry.com",
        
        # Branding & Media
        logo_url=None,  # Add logo URL if you have one
        hero_image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuAdsrlIdyBHH5LqfXHXGtHqm24viU0ioFujJ-RZmf4jTEnhjXFdVQ188aA9Ysf1_VLFewh-MYNRETUoHOWv8CunSTc1SeQm9ixrfVn-sqaefWY07I4V4-DsF1IkPvd5TY_8fnB70rlrjI8HeZLR7iIXC0RuYgaNO4W7ve8qWnogeaOmfQugYglmBzII7o-UmYhrmjm-vUywo46hyoO8dBPsM6YcWydBw-xk1-UYuIkiC20HfBIn3atDrxZwv9D_6WkN-Evevdc1_x2F",
        about_image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuCDOe9z56owu9TgP3lHYSF-quDFp7o1Zd2_0sAryJYPR7_xbr0CBuMWgEzWQNol7naaoJheGOa8guWKuIRTD1x8ToyHcOtPtq07U7ZpjK_cDPVFyYUZepPVJfliJUQuZBRRvotnIgpWf9_iBzOg9I-GwAF92jUlrqXjyG-EAqltnik5ZooA4PFVMvvWv7XlSwy9hS-rF1hu7GeOb4kuGn_zS6yTZpFyb_16hqmZBlUrlbiyRqSgz_R7tyX5qcXkN0tSqXw-rG9Uw3Hn",
        owner_image_url="https://lh3.googleusercontent.com/aida-public/AB6AXuD3S1Eprs9v5t8UMmOSbQVdTWHWhjDOOgK_Rz75Cn5q40FG5J77NF78AaxIyidfYmjeA1thI8CZx3_2sS7Xg0j8jr4jCrUowfaPC-hvtdBME_NfFzIiCUngQLlpHEOMXIv7tGt3k9wdA3M-eIZhggOzL09Ip5W1TcvDyBiQhaCmmVEG28a0ghuHdTl5e18lYX6Tvf4Ri2FY3ZP_JbQEBJmlVBIHf0f9SKioYXDfjVNBFGq84_lGJvSFWH0COtnKoEtDmVVocEsitaOX",
        
        # About Section
        story="Kurdie's Curry is a culinary journey that blends the vibrant spices of India with the rich, comforting flavors of Kurdistan. Our story began with a dream to share the unique dishes from our two cultures, creating a dining experience that is both familiar and excitingly new.",
        cuisine_type="Indian-Kurdish Fusion",
        owner_name="Amrita Patel",
        owner_bio="Amrita's passion for food is rooted in her dual heritage. Growing up in a family that celebrated both Indian and Kurdish traditions, her kitchen was always a place of discovery. With Kurdie's Curry, she brings her family's legacy to your table, sharing the love and flavors that shaped her life.",
        
        # Business Details
        business_hours={
            0: None,  # Sunday - CLOSED
            1: (11, 21),  # Monday: 11am-9pm
            2: (11, 21),  # Tuesday
            3: (11, 21),  # Wednesday
            4: (11, 21),  # Thursday
            5: (11, 22),  # Friday: 11am-10pm
            6: (11, 22),  # Saturday: 11am-10pm
        },
        menu=kurdies_menu,
        
        # Settings
        is_active=True,
        accepts_reservations=True,
    )
    
    restaurants.append(kurdies_curry)
    
    return restaurants
