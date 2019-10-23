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
import { mapState, mapActions } from "vuex"

export default {
    data(){
        return{
        items: [
        {
          src: 'https://i.ytimg.com/vi/9qHgYd_EBYw/maxresdefault.jpg',
        },
        {
          src: 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F99A01B415ADFDB991B50CC',
        },
        {
          src: 'https://www.jobaba.net/file/image.do?filePath=sONy7CFJVlHd+/JjdwFq+uxcZohtu3Wu0iMLSL7EjWGKA9yOYw26ZcGfvA/RxpdG',
        },
        {
          src: 'data:image/png;base64,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',
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