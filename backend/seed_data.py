#!/usr/bin/env python3
"""
Seed Database with Sample Data
Populates restaurant and menu data from sample_data.py into database
"""
import sys
from app.database.base import SessionLocal
from app.database.models import RestaurantModel, MenuItemModel
from app.data.sample_data import create_sample_restaurants

def seed_database():
    """Populate database with sample restaurant and menu data"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_restaurants = db.query(RestaurantModel).count()
        if existing_restaurants > 0:
            print(f"⚠️  Database already has {existing_restaurants} restaurant(s)")
            response = input("Do you want to clear and re-seed? (yes/no): ")
            if response.lower() != 'yes':
                print("❌ Cancelled")
                return
            
            # Clear existing data
            print("🗑️  Clearing existing data...")
            db.query(MenuItemModel).delete()
            db.query(RestaurantModel).delete()
            db.commit()
            print("✅ Existing data cleared")
        
        # Load sample data
        print("📦 Loading sample data...")
        restaurants = create_sample_restaurants()
        
        for restaurant in restaurants:
            print(f"\n📍 Seeding {restaurant.name}...")
            
            # Create restaurant
            db_restaurant = RestaurantModel(
                id=restaurant.id,
                name=restaurant.name,
                slug=restaurant.slug,
                tagline=restaurant.tagline,
                address=restaurant.address,
                phone=restaurant.phone,
                email=restaurant.email,
                logo_url=restaurant.logo_url,
                hero_image_url=restaurant.hero_image_url,
                about_image_url=restaurant.about_image_url,
                owner_image_url=restaurant.owner_image_url,
                story=restaurant.story,
                cuisine_type=restaurant.cuisine_type,
                owner_name=restaurant.owner_name,
                owner_bio=restaurant.owner_bio,
                business_hours={str(k): v for k, v in restaurant.business_hours.items()},  # Convert keys to strings for JSON
                is_active=restaurant.is_active,
                accepts_reservations=restaurant.accepts_reservations
            )
            db.add(db_restaurant)
            print(f"  ✅ Restaurant '{restaurant.name}' added")
            
            # Create menu items
            menu_items_count = 0
            for item in restaurant.menu.items:
                db_menu_item = MenuItemModel(
                    restaurant_id=restaurant.id,
                    name=item.name,
                    description=item.description,
                    price=item.price,
                    category=item.category.value,  # Convert enum to string
                    tags=[tag.value for tag in item.tags],  # Convert enums to strings
                    image=item.image,
                    is_available=True,
                    display_order=item.id
                )
                db.add(db_menu_item)
                menu_items_count += 1
            
            print(f"  ✅ {menu_items_count} menu items added")
        
        # Commit all changes
        db.commit()
        
        # Verify
        print("\n" + "="*60)
        print("✅ Database seeded successfully!")
        print("="*60)
        
        restaurant_count = db.query(RestaurantModel).count()
        menu_item_count = db.query(MenuItemModel).count()
        
        print(f"\n📊 Summary:")
        print(f"  Restaurants: {restaurant_count}")
        print(f"  Menu Items:  {menu_item_count}")
        print(f"\n💡 Your restaurant data is now in the database!")
        print(f"   You can query it using the API or check_database.py\n")
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        db.rollback()
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    finally:
        db.close()

if __name__ == '__main__':
    print("🌱 Database Seeder")
    print("="*60)
    seed_database()

