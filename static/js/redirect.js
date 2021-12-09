/* var URLdomain = window.location.host;
//alert(URLdomain);
console pathname = window.location.pathname;
//alert(pathname);
const URLactual = window.location.href;
const URLactual2 = window.location.search; */

function cargando() {
  document.getElementById("cargando").style.display = "block";
  document.getElementById("info_video").style.display = "none";
}

function descargarVideo(data) {
  const videoR = document.getElementById("videoR");
  document.getElementById("cargando").style.display = "block";

  url = {
    host: window.location.host,
    search: window.location.search,
  };
  if (url.search.length > 25) {
    idVideo = url.search.split("%");
    url.search = idVideo[6].slice(2);
  } else {
    idVideo = url.search.split("=");
    url.search = idVideo[1];
  }
  console.log(url.search);

  url = `http://${url.host}/key-download?detailSearch=${url.search}&key-id=${data.format_id}&key-ext=${data.format_ext}`;
  console.log(url);
  fetch(url)
    .then((res) => res.json())
    .then((response) => {
      videoR.style.display = "block";
      console.log(response)
      if (response.url == null) {
        videoR.innerHTML = "<h1>Error</h1>";
      } else {
        
        format_ext = data.format_ext;
        document.getElementById("cargando").style.display = "none";
        /*  <audio class='embed-responsive-item' controls >
            <source src="${response.url}">
          </audio>
           */
        if (format_ext == "mp3") {
          clase='modal-dm'
          detalle = `
          <div class="card mx-auto border-0" style="width: 22rem;">
            <img class="card-img-top" src="../static/img/music.svg" alt="Card image cap">
            <div class="card-body embed-responsive-item">
              <audio  controls>
                  <source src="${response.url}"> 
                </audio>
            </div>
          </div>
          `;
        } else {
          clase='modal-lg'
          detalle=
          `
          <div class="ratio  ratio-16x9" >
            <video class="embed-responsive-item "  controls>
              <source src="${response.url}"> 
            </video><!---->
          </div> 
          `
        }


        
        videoR.innerHTML = `
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#resultado">
          Mi descarga...
        </button>
        <div class="modal fade" id="resultado" tabindex="-1" aria-labelledby="resultadoLabel" aria-hidden="true">
          <div class="modal-dialog ${clase}">
            <div class="modal-content ">
              <div class="modal-body p-0 m-0 ">
               ${detalle}
              </div>
              <div class="modal-footer mb-0">
                <span class="mr-4">
                ${response.title}
                </span>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>


        

         `;
        // Create a new link
        const link = document.createElement("a");
        link.download = "file name";
        link.href = response.url;

        // Append to the document
        document.body.appendChild(link);

        // Trigger the click event
        link.click();

        // Remove the element
        document.body.removeChild(link);

      }
      //type="video/mp4"
      /*if (data.format_ext === "MP3") {
        
      } else {
        videoR.innerHTML = `
            <audio width="320" height="240" controls >
               <source src="${response.url}">
            </audio>
         `;
      }

      // Create a new link
       */
    });

  /*fetch('http://localhost:5000/descargar-video?url={{ url }}')
                .then(res => res.json())
                .then(response => {
                    cargando.style.display = 'none';
                    const link = document.createElement("a");
                    link.download = 'video';
                    link.href = response.url;
                    link.click();
                })
                 */
  //http://127.0.0.1:5000/video?detailSearch=my+universe
}
