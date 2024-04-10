 with open("/deneme.jpeg", "w+b") as f:
            supabase.storage.from_("testbucket").upload(f, f)