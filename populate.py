import os
import re

ASSETS_DIR = os.path.join("assets", "pictures")
FOLDERS_MAP = {
    "RUNWAY": ("runway", "Runway Flow"),
    "FASHION CAMPAIGN": ("editorial", "Campaign Shoot"),
    "AWARDS'": ("awards", "Awards & Titles"),
    "JUDGING EVENT": ("events", "Event Judge"),
    "TEAM  BUILDING": ("events", "Event Management"),
    "TRAINING": ("training", "Model Training")
}

def generate_gallery_html():
    if not os.path.exists(ASSETS_DIR):
        print(f"Error: {ASSETS_DIR} not found.")
        return ""
    
    html_items = []
    
    for folder, config in FOLDERS_MAP.items():
        folder_path = os.path.join(ASSETS_DIR, folder)
        if not os.path.exists(folder_path):
            continue
            
        data_category = config[0]
        base_cat_name = config[1]
        
        valid_exts = {".jpg", ".jpeg", ".png", ".webp"}
        
        files = [f for f in os.listdir(folder_path) if os.path.splitext(f.lower())[1] in valid_exts]
        
        # Optionally skip files with redundant names or duplicates by hash if needed, but we rely on files provided.
        for file in files:
            file_rel_path = f"assets/pictures/{folder}/{file}"
            # URL encode single quotes if needed
            file_url_path = file_rel_path.replace("AWARDS'", "AWARDS%27")
            
            # Construct standard, extremely clean structure
            item = f'''
          <article class="gallery-card reveal reveal-up" data-category="{data_category}">
            <img src="{file_url_path}" alt="{base_cat_name}" loading="lazy">
            <button class="gallery-overlay" data-full="{file_url_path}" aria-label="Open {base_cat_name}">
              <span>{base_cat_name}</span>
            </button>
          </article>'''
            html_items.append(item)
            
    return "\\n".join(html_items)

def apply_patch():
    # 1. Update HTML
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    gallery_html = generate_gallery_html()
    
    # Notice we replace exactly the `.gallery-grid` content from old indexing
    html = re.sub(
        r'<div class="gallery-grid">.*?</div>\s*</div>\s*</section>',
        f'<div class="gallery-grid">\\n{gallery_html}\\n        </div>\\n      </div>\\n    </section>',
        html,
        flags=re.DOTALL
    )
    
    # Ensure TikTok wraps look pro
    # Let's verify we have tiktok embeds 
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    # 2. Update CSS for premium TikTok and Gallery sizing
    css_patch = """
/* PRO TIKTOK EMBED WRAPPER */
.tiktok-embed-wrapper {
   position: relative;
   border-radius: 14px;
   overflow: hidden;
   box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
   border: 1px solid rgba(214, 185, 106, 0.3);
   background: #000;
   transition: transform 0.4s ease, box-shadow 0.4s ease;
   max-width: 325px;
   margin: 0 auto;
}
.tiktok-embed-wrapper:hover {
   transform: translateY(-8px);
   box-shadow: 0 15px 50px rgba(214, 185, 106, 0.3);
   border-color: rgba(214, 185, 106, 0.7);
}

/* SMART GALLERY SIZING */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.2rem;
    align-items: start;
}
.gallery-card {
    margin-bottom: 0; 
    border-radius: 8px;
    height: 100%;
}
.gallery-card img {
    width: 100%;
    height: 380px; 
    object-fit: cover; 
    border-radius: 8px;
    filter: brightness(0.9);
    transition: filter 0.4s, transform 0.6s cubic-bezier(0.2, 1, 0.3, 1);
}
.gallery-card:hover img {
    filter: brightness(1.1);
    transform: scale(1.05);
}
"""
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(css_patch)

    print("Populated all images and styled TikTok.")

if __name__ == '__main__':
    apply_patch()
