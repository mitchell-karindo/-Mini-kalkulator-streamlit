import streamlit as st
import math
from datetime import datetime

def kalkulator_opr(num1, num2, opr):
    """
    Fungsi untuk melakukan operasi matematika
    """
    try:
        if opr == '+': 
            res = num1 + num2
        elif opr == '-': 
            res = num1 - num2
        elif opr == '*': 
            res = num1 * num2
        elif opr == '/': 
            if num2 == 0:
                return "Error: Pembagian dengan nol"
            res = num1 / num2
        elif opr == '%': 
            if num2 == 0:
                return "Error: Modulo dengan nol"
            res = num1 % num2
        elif opr == '^': 
            res = num1 ** num2
        elif opr == '√':
            if num1 < 0:
                return "Error: Akar dari bilangan negatif"
            res = math.sqrt(num1)
        return res
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Konfigurasi halaman
    st.set_page_config(
        page_title="Kalkulator",
        page_icon="🧮",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # CSS untuk styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .history-item {
        padding: 0.5rem;
        border-bottom: 1px solid #ddd;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        color: #6c757d;
    }
    .stButton button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar untuk informasi project
    with st.sidebar:
        st.title("Tentang Project")
        st.info("""
        Ini adalah mini project kalkulator yang dibangun dengan Streamlit.
        
        **Fitur:**
        - Operasi matematika dasar
        - Riwayat perhitungan
        - Tampilan responsif
        - Antarmuka pengguna yang intuitif
        
        Dibuat untuk Mini Project.
        """)
        
        st.markdown("---")
        st.markdown("### 📊 Statistik")
        if 'total_calculations' not in st.session_state:
            st.session_state.total_calculations = 0
        st.write(f"Total Perhitungan: **{st.session_state.total_calculations}**")
        
        st.markdown("---")
        st.markdown("### 📝 GitHub")
        st.markdown("Ingin lihat project yang lain klik [GitHub](https://github.com/mitchell-karindo)")
    
    # Header aplikasi
    st.markdown('<h1 class="main-header">🧮 Kalkulator Streamlit</h1>', unsafe_allow_html=True)
    st.caption("Mini Project Kalkulator")
    
    # Inisialisasi session state untuk riwayat
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'total_calculations' not in st.session_state:
        st.session_state.total_calculations = 0
    
    # Layout dengan columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="sub-header">Input Bilangan</div>', unsafe_allow_html=True)
        
        # Input bilangan
        num1 = st.number_input("Masukkan bilangan pertama:", value=0.0, step=1.0, format="%g")
        
        # Pilih operasi
        operation = st.selectbox(
            "Pilih operasi:",
            ["Penambahan (+)", "Pengurangan (-)", "Perkalian (*)", "Pembagian (/)", 
             "Sisa Bagi (%)", "Pangkat (^)", "Akar Kuadrat (√)"]
        )
        
        # Tampilkan input bilangan kedua jika bukan akar kuadrat
        if "Akar Kuadrat" not in operation:
            num2 = st.number_input("Masukkan bilangan kedua:", value=0.0, step=1.0, format="%g")
        else:
            num2 = 0  # Tidak digunakan untuk akar kuadrat
    
    with col2:
        st.markdown('<div class="sub-header">Operasi</div>', unsafe_allow_html=True)
        
        # Konversi pilihan operasi ke simbol
        op_dict = {
            "Penambahan (+)": '+',
            "Pengurangan (-)": '-',
            "Perkalian (*)": '*',
            "Pembagian (/)": '/',
            "Sisa Bagi (%)": '%',
            "Pangkat (^)": '^',
            "Akar Kuadrat (√)": '√'
        }
        
        operator = op_dict[operation]
        
        # Tampilkan operasi yang dipilih
        st.info(f"Operasi: **{operator}**")
        
        # Tombol hitung
        if st.button("Hitung", type="primary", use_container_width=True):
            if operator == '√':
                result = kalkulator_opr(num1, num2, operator)
                operation_str = f"√{num1}"
            else:
                result = kalkulator_opr(num1, num2, operator)
                operation_str = f"{num1} {operator} {num2}"
            
            # Simpan ke riwayat dengan timestamp
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.session_state.history.append({
                "operation": operation_str,
                "result": result,
                "time": timestamp
            })
            
            # Update total perhitungan
            st.session_state.total_calculations += 1
            
            # Tampilkan hasil
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.success(f"**Hasil:** {operation_str} = **{result}**")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Riwayat perhitungan
    st.markdown("---")
    st.markdown('<div class="sub-header">Riwayat Perhitungan</div>', unsafe_allow_html=True)
    
    if st.session_state.history:
        # Tampilkan hanya 5 riwayat terakhir
        for calc in reversed(st.session_state.history[-5:]):
            st.markdown(f"""
            <div class="history-item">
                <b>{calc['operation']} = {calc['result']}</b>
                <div style="font-size: 0.8rem; color: #6c757d;">{calc['time']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada riwayat perhitungan")
    
    # Tombol clear history
    if st.session_state.history:
        if st.button("Hapus Riwayat", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div class="footer">
            Dibuat oleh Mitchell Karindo menggunakan Streamlit | © 2025 Mini Project Kalkulator
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()