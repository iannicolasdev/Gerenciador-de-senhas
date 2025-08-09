import random 
import string as st

caracteres = st.ascii_letters + st.digits + st.punctuation

print(''.join(random.choices(caracteres, k=12)))