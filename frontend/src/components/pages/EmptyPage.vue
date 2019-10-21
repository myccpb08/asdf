<!-- MainPage -->
<template>
<div> 
    <v-container>
        <v-layout>
            <v-flex>
                <div style="width: 80%; height:  margin-top:5px; text-align:center;">
                        <!-- Slideshow container -->
                    <v-carousel>
                        <v-carousel-item
                            v-for="(item,i) in items"
                            :key="i"
                            :src="item.src"
                            reverse-transition="fade-transition"
                            transition="fade-transition"
                        ></v-carousel-item>
                    </v-carousel>
                </div>
            </v-flex>
        </v-layout>
    </v-container>
    
  </div>
</template>
<script>

    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
    showSlides(slideIndex += n);
    }

    function currentSlide(n) {
    showSlides(slideIndex = n);
    }

   
</script>
<script>
import { mapState, mapActions } from "vuex";
export default {
    data(){
        return{
        items: [
        {
          src: 'http://www.jejuyouth.com/services/announce.htm?act=download&seq=2201&no=1',
        },
        {
          src: 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F99A01B415ADFDB991B50CC',
        },
        {
          src: 'https://www.jobaba.net/file/image.do?filePath=sONy7CFJVlHd+/JjdwFq+uxcZohtu3Wu0iMLSL7EjWGKA9yOYw26ZcGfvA/RxpdG',
        },
        {
          src: 'https://i.ytimg.com/vi/9qHgYd_EBYw/maxresdefault.jpg',
        }
        ]
        }
    },
  components: {
  },
    methods:{
        showSlides(n){
            
        }
    }
};

</script>
<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
    max-width: 1000px;
    height:350px;
    position: relative;
    margin: auto;
}

/* Hide the images by default */
.mySlides {
    height: 350px;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* Caption text */
.text {
    color: #f2f2f2;
    font-size: 15px;
    padding: 8px 12px;
    position: absolute;
    bottom: 8px;
    width: 100%;
}

/* Number text (1/3 etc) */
.numbertext {
    height: 350px;
    color: #f2f2f2;
    font-size: 12px;
    padding: 8px 12px;
    position: absolute;
    top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}

</style>
