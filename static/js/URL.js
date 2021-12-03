$(document).ready(function () {
    const data ={
        maxResults: 10,
        key:'AIzaSyDgX0YXt8ztGqFDJA5CS1kHTPHaDQxYv70',
        part: 'snippet',
        q: 'kTJczUoc26U',
        type: 'video'
    }
    $.getJSON('https://www.googleapis.com/youtube/v3/search', data,function(res){
        //console.log(res)
        $(res.items).each(function(){

            console.log(this);
            var thumbnail = this.snippet.thumbnails.high.url;
            var title = this.snippet.title;
            var description = this.snippet.description;
            var id = this.id.videoId;
            var video = $(`
            <div class="col ">
                <div class='p-4 border bg-light'>
                    <div class="card border-0" style="width: auto;" id=${id}>
                        <a href="https://www.youtube.com/watch?v=${id}">
                            <img class="card-img-top" src=" ${thumbnail} " alt="${title}" >
                        </a>
                        <div class="card-body">
                            <h5 class="card-title"> ${title} </h5>
                            <p class="card-text">${description }</p>
                        </div>
                        <div class="card-header text-center">
                        <button type="button" class="btn btn-primary" value=${id} id="mp3">
                        <i class="fa fa-file-audio-o" aria-hidden="true"></i>
                         MP-3
                        </button>
                        <button type="button" class="btn btn-info"  id="mp4" value=${id}>
                        <i class="fa fa-file-video-o" aria-hidden="true"></i> 
                            MP-4
                        </button>
                        </div>
                    </div>
                </div>
            </div>`
            );
            $("#video-list").append(video);
          //
          /* 
          '<div class="video row" data-video-id="' + id + '"> <div class="thumbnail col-lg-5 col-md-5 col-sm-5 col-12"> <img src="' + thumbnail + '" alt="Thumbail"> </div><div class="video-info col-lg-7 col-md-7 col-sm-7 col-12"> <h3>' + title + '</h3> <div class="description"> <p>' + description + '</p></div></div></div>'
        `<div class="p-3 border bg-light">
            <div class="card" style="width: auto;">
                <img class="card-img-top" src=" ${thumbnail} " alt="${title}" src="https://www.youtube.com/watch?v=${i}">
                <div class="card-body">
                    <h5 class="card-title"> ${title} </h5>
                    <p class="card-text">{$description }</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>`
          */
        });
    })
}
);