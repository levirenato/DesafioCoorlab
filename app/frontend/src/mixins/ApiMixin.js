import { ref } from "vue";
export default{
    data(){
        return {
            selectedDate : ref(),
            selectedCity : ref(),
            transports : [],
            }
          },

          methods:{
            validation() {
              if(this.selectedDate == undefined | this.selectedCity == undefined){
                  return true
              }
             else{
                 this.$router.replace(
                  `/search/${this.selectedCity.city}/`
                  );
                  return false
              }
          },
            getTransport(url){
              fetch(url)
              .then(res => res.json())
              .then(data => this.transports = data)
            },
            clearData(){
              this.selectedCity = ref()
              this.selectedDate = ref()
          },
          },
}