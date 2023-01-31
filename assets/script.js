/* Search Bar */
      
      document.querySelector('#cari').addEventListener('keyup', function(e) {
          // UI Element
          let surat = document.getElementsByClassName('border');
      
          // Get Search Query
          let searchQuery = cari.value.toLowerCase();
      
          // Search Compare & Display
          for (let index = 0; index < surat.length; index++) {
                  const border = surat[index].textContent.toLowerCase();
      
                  if (border.includes(searchQuery)) {
                          surat[index].style.display = 'block';
                  } else {
                          surat[index].style.display = 'none';
                  }
          }
      });
