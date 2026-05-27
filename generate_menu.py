import re

def create_item(name, price, desc=""):
    desc_html = f'<p class="menu-item-desc">{desc}</p>' if desc else ""
    return f"""
            <div class="menu-item-row" data-aos="fade-up">
              <div class="menu-item-header">
                <span class="menu-item-name">{name}</span>
                <span class="menu-item-price">{price}</span>
              </div>
              {desc_html}
            </div>"""

def create_block(title, items, image_url, image_on_left=False, two_col=False):
    grid_class = "menu-items-grid two-col" if two_col else "menu-items-grid"
    content_html = f"""
        <div class="menu-content-block">
          <h3 class="menu-category-title" data-aos="fade-down">{title}</h3>
          <div class="{grid_class}">
            {''.join(items)}
          </div>
        </div>"""
        
    image_html = f"""
        <div class="menu-image-block">
          <img src="{image_url}" alt="{title}">
        </div>"""
        
    if image_on_left:
        inner_html = image_html + content_html
    else:
        inner_html = content_html + image_html
        
    return f"""
      <div class="menu-row">
        {inner_html}
      </div>"""

# 1. SOUP
soup_items = [
    create_item("Clear Soup (Veg / Chicken)", "₹170/210", "A light flavourful broth made with chicken, herbs, vegetables and mild seasonings."),
    create_item("Hot & Sour Soup (Veg / Chicken)", "₹180/210", "A spicy and tangy soup, usually made with mixed vegetables or chicken, balanced with spicy and tangy flavors."),
    create_item("Manchow Soup (Veg / Chicken)", "₹190/210", "A spicy Indo-Chinese soup made with mixed vegetables or chicken and spices, usually topped with crispy fried noodles."),
    create_item("Sweet Corn Soup (Veg / Chicken)", "₹180/210", "A mild creamy, slightly sweet soup made with corn, broth, and mixed vegetables or Chicken."),
    create_item("Tom Yum Soup (Veg / Sea Food Soup)", "₹190/240", "A thai style hot n spicy, tangy flavor, using herbs, lime, and aromatic spices with veg or chicken."),
    create_item("Cream Soup (Tomato / Mushroom / Chicken)", "₹180/200/220", "A rich and creamy soup made with tomatoes/chicken/mushroom."),
    create_item("Talumein Soup (Veg / Chicken)", "₹200", "A hearty noodles soup wth mixed vegetables or tender chicken with aromatic spices."),
    create_item("Chicken Lung Fung Soup", "₹210", "A rich, thick Chinese-style soup made with chicken, vegetables, silky egg strands, and its smooth texture and savory taste."),
    create_item("Chettinad Mutton Soup", "₹230", "A spicy South Indian soup, made with Chettinad spices, pepper, and mutton, known for its bold and flavorful taste.")
]
soup_block = create_block("SOUP", soup_items, "https://supremehospitals.in/wp-content/uploads/2026/05/soups-scaled.jpg", image_on_left=False)

# 2. STARTER
starter_items = [
    create_item("Barbecue Chicken (Full/Half)", "₹570/325", "A Middle Eastern Spicy chicken dish, chicken marinated with barbeque sauce, spices and cooked over charcoal for a smoky flavor."),
    create_item("Al Faham Dejaj (Chicken) (Full/Half)", "₹570/325", "A Middle Eastern non spicy chicken dish, marinated with Arabian sauce, spices and cooked over charcoal for a smoky flavor."),
    create_item("Pepper Barbeque (Chicken) (Full/Half)", "₹570/325", "A spicy barbeque dish flavored with black pepper and spices, usually roasted over the charcoal heat for a bold, smoky taste."),
    create_item("Filipino BBQ(Chicken) (Full/Half)", "₹580/335", "A sweet and savory chicken dish from Philippines, marinated in soy sauce, garlic, sugar, and spices, then cooked over charcoal for a smoky flavor."),
    create_item("Grill Chicken (Full/half)", "₹550/300", "Chicken cooked with skin over the direct flame, often marinated with spices, giving it a smoky flavor and juicy texture."),
    create_item("Laham Nashif (Bone less Mutton Cubes)", "₹650", "A Middle Eastern dry meat dish made with tender pieces of lamb, cooked with spices, onions for a rich, savory flavor."),
    create_item("Laham Meshwi (Mutton)", "₹650", "A Middle Eastern grilled meat dish (usually lamb), marinated with spices and cooked on a flat pan (tawa) for a smoky, juicy flavor."),
    create_item("Samak Al Faham (Barbeque-Fish)", "₹700", "A Middle Eastern whole fish marinated in spiced charcoal-grill seasoning, then flame-grilled for a smoky, juicy flavor."),
    create_item("Samak Tawa (Vanjaram Fish)", "₹1800", "A whole fish where marinated with Arabian masala and shallow-fried on a flat pan (tawa) with spices, giving it a crispy outside and flavorful taste."),
    create_item("Grilled King Fish", "₹As Per Size", "King fish marinated with Arabian spices and grilled over heat, giving it a smoky flavor and tender, juicy texture."),
    create_item("Fish Fry (Vanjaram)", "₹350", "Fish marinated with spices and shallow fried until crispy on the outside and tender inside."),
    create_item("Rubiyan Faa/ Meshwi (Prawn)", "₹650/650", "A Middle Eastern style (shrimp) dish, lightly spiced and typically fried or sautéed for a flavorful, juicy taste."),
    create_item("Squid Tawa Fry", "₹500", "Squid pieces marinated with spices and shallow-fried on a tawa, giving a crispy texture and rich, spicy flavor.")
]
starter_block = create_block("STARTER (ARABIAN)", starter_items, "https://supremehospitals.in/wp-content/uploads/2026/05/grill-scaled.jpg", image_on_left=True)

# 3. RICE & BIRYANI
rice_items = [
    create_item("Steam Rice", "₹160"), create_item("Ghee Rice", "₹200"),
    create_item("Curd Rice", "₹180"), create_item("Egg Biryani", "₹250"),
    create_item("Veg.Biryani", "₹220"), create_item("Chicken Dum Biryani", "₹310"),
    create_item("Veg.Pulao", "₹220"), create_item("Chicken 65 Biryani (Boneless)", "₹330"),
    create_item("Cashewnut Pulao", "₹250"), create_item("Mutton Dum Biryani", "₹375"),
    create_item("Kashmiri Pulao", "₹250"), create_item("Fish Biryani", "₹390"),
    create_item("Paneer Pulao", "₹275"), create_item("Prawns Biryani", "₹410")
]
rice_block = create_block("RICE & BIRYANI", rice_items, "https://supremehospitals.in/wp-content/uploads/2026/05/briyani-scaled.jpg", image_on_left=False, two_col=True)

# 4. CHINESE RICE / NOODLE
chinese_items = [
    create_item("Veg Fried Rice", "₹210"), create_item("Veg Noodle", "₹240"),
    create_item("Veg Schezwan Fried Rice", "₹220"), create_item("American Chicken Chopsuey", "₹300"),
    create_item("Mushroom Fried Rice", "₹250"), create_item("Veg Hakka Noodle", "₹250"),
    create_item("Egg Fried Rice", "₹230"), create_item("Chinese Chicken Chopsuey", "₹300"),
    create_item("Chicken Fried Rice / Schezwan", "₹260/220"), create_item("Noodles (Chicken / Mix)", "₹280/330"),
    create_item("Mix Fried Rice / Schezwan", "₹310/320"), create_item("Chicken Hakka Noodle", "₹300"),
    create_item("Singapuri Fried Rice", "₹300/350"), create_item("Schezwan Noodle", "₹300/350"),
    create_item("Veg Chilli Garlic Noodle", "₹270"), create_item("Chilli Garlic Noodle", "₹300/350"),
    create_item("Veg Schezwan Noodle", "₹250"), create_item("Pan Fried Noodle (Chicken / Mix)", "₹350/400"),
    create_item("American Veg. Chopsuey", "₹280"), create_item("Singapuri Noodle", "₹300/350"),
    create_item("Chinese Veg Chopsuey", "₹280"), create_item("Egg Noodles", "₹260"),
    create_item("Egg Hakka Noodle", "₹260")
]
chinese_block = create_block("CHINESE RICE & NOODLES", chinese_items, "https://supremehospitals.in/wp-content/uploads/2026/05/fired-rice-scaled.jpg", image_on_left=True, two_col=True)

# 5. BREAD
bread_items = [
    create_item("Kerala Paratha/ Chapathi/ Butter Chapathi", "₹60/40/55"),
    create_item("Tandoori Paratha", "₹60"),
    create_item("Pudina Paratha", "₹70"),
    create_item("Methi Paratha", "₹70"),
    create_item("Kubus", "₹30"),
    create_item("Naan (Plain / Butter / Garlic/ Cheese )", "₹60/70/80/90"),
    create_item("Kulcha (Plain / Butter/ Masala / Paneer )", "₹60/70/80/90"),
    create_item("Tandoori Roti (Plain/ Butter / Garlic )", "₹50/60/70"),
    create_item("Bread Basket", "₹300")
]
bread_block = create_block("BREAD", bread_items, "https://supremehospitals.in/wp-content/uploads/2026/05/Naan-scaled.jpg", image_on_left=False)

# 6. INDIAN GRAVY
gravy_items = [
    create_item("Egg Masala / Roast", "₹200"), create_item("Chicken Bhukara", "₹370"),
    create_item("Chicken Curry/ Masala", "₹340"), create_item("Mutton Korma/Masala", "₹460"),
    create_item("Chicken Pepper Masala", "₹350"), create_item("Mutton Pepper Masala", "₹460"),
    create_item("Chicken Chettinadu", "₹350"), create_item("Mutton Chettinadu", "₹460"),
    create_item("Kadai Chicken", "₹360"), create_item("Mutton Roganjosh", "₹460"),
    create_item("Chicken Roganjosh", "₹360"), create_item("Mutton Kadai", "₹460"),
    create_item("Chicken Korma", "₹360"), create_item("Mutton Mughlai", "₹470"),
    create_item("Chicken Butter Masala", "₹370"), create_item("Fish Chettinadu", "₹440"),
    create_item("Chicken Coriander Gravy", "₹370"), create_item("Kerala Fish Masala", "₹440"),
    create_item("Chicken Tikka Masala", "₹380"), create_item("Squid Roast", "₹450"),
    create_item("Chicken Sagoti", "₹380"), create_item("Prawn Pepper Masala", "₹460"),
    create_item("Chicken Mughlai", "₹380"), create_item("Kadai Prawn", "₹460"),
    create_item("Chicken Chingari", "₹380"), create_item("Prawn Chettinadu", "₹460")
]
gravy_block = create_block("INDIAN GRAVY (NON-VEG)", gravy_items, "https://supremehospitals.in/wp-content/uploads/2026/05/chicken-gravy-scaled.jpg", image_on_left=False, two_col=True)

# 7. BURGER & SANDWICH
burger_items = [
    create_item("Veg Burger", "₹150"), create_item("Veg Cheese Burger", "₹170"),
    create_item("Chicken Burger", "₹200"), create_item("Chicken Cheese Burger", "₹220"),
    create_item("Sandwich (Tomato/Veg Grill/Veg Cheese)", "₹100/120/140"), create_item("Egg Sandwich", "₹120"),
    create_item("Grilled Chicken Sandwich", "₹150"), create_item("Chicken Cheese Sandwich", "₹160"),
    create_item("Club Chicken Sandwich", "₹260")
]
burger_block = create_block("BURGER & SANDWICH", burger_items, "https://supremehospitals.in/wp-content/uploads/2026/05/07-scaled.jpg", image_on_left=True, two_col=True)

# 8. ICE-CREAM
icecream_items = [
    create_item("Vanilla/Strawberry", "₹150"), create_item("Chilli Guava", "₹130"),
    create_item("Chocolate", "₹160"), create_item("Mini Falooda", "₹180"),
    create_item("Butter Scotch", "₹160"), create_item("Gem Favorite Ice-cream", "₹250"),
    create_item("Kesar Pistha", "₹180"), create_item("Royal Falooda", "₹220"),
    create_item("Real Orange", "₹170"), create_item("Fruit Salad", "₹200/180", "With Ice Cream & W/O Ice cream"),
    create_item("Real Mango", "₹180"), create_item("Sizzling Brownie", "₹320"),
    create_item("Matka Kulfi", "₹80"), create_item("Turkish Kunafa", "₹450"),
    create_item("Casata Bar", "₹120")
]
icecream_block = create_block("ICE-CREAM", icecream_items, "https://supremehospitals.in/wp-content/uploads/2026/05/ice-cream-scaled.jpg", image_on_left=False, two_col=True)

# Final CTA
cta_block = """
    <section class="menu-cta-section" data-aos="zoom-in" data-aos-duration="1500">
      <h2 class="menu-cta-text">"Even more... lots and lots of variety of dishes are there to taste. Visit and explore GEM Restaurant."</h2>
      <p class="menu-cta-sub">A Culinary Experience Awaits</p>
    </section>
"""

new_menu_html = f"""
    <section id="menu" class="gem-menu-new">
      <div class="menu-showcase-container">
        {soup_block}
        {starter_block}
        {rice_block}
        {chinese_block}
        {bread_block}
        {gravy_block}
        {burger_block}
        {icecream_block}
      </div>
      {cta_block}
    </section>
"""

# Read gem.html and replace <section id="menu"> ... </section>
filepath = r"d:\Rk hospitality\gem.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace menu section
new_content = re.sub(r'<section id="menu".*?</section>', new_menu_html, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Menu generated and injected into gem.html successfully.")
