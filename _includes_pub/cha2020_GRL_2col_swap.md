

### Cha, T-Y., M. M. Bell, W.-C. Lee, A. J. DesRosiers, 2020: Polygonal Eyewall Asymmetries during the rapid intensification of Hurricane Michael (2018), In prep.  

<!--p>&nbsp;</p-->
---
<style>

div.ex3 {

  height: 400px;
  overflow: auto;
}

a.buttonswap {
  display:block;
  width:100px;
  height:50px;
  background-color:#424242;
  color:#fff;
  line-height:50px;
  text-align:center;
  text-decoration: none;
  margin: 1px;
}

a.active {
  background-color:red;
}

.subcontent {

}

div[class*="subcontent-"] {
  display:none;
}

div.active {
  display:block;
}
</style>
<script>
    $('.buttonswap').first().addClass('active');

    $('.buttonswap').click(function(){
      var $this = $(this);
      $siblings = $this.parent().children(),
      position = $siblings.index($this);
      console.log (position);

      $('.subcontent div').removeClass('active').eq(position).addClass('active');

      $siblings.removeClass('active');
      $this.addClass('active');
    })
</script>

<div class="row">
  <div class="6u 12u$(medium) exp3 subcontent">
  <div class="subcontent-1 active">
  <center> <h3>Abstract</h3> </center>
    <center>  
    <p class="align-justify">
    Hurricane Matthew (2016) was observed by the NEXRAD KAMX polarimetric radar and NOAA P-3 airborne radar near the coast of the southeastern United States for several hours, providing a novel opportunity to evaluate and compare single and multiple Doppler wind retrieval techniques for tropical cyclone flows.
    The generalized velocity track display (GVTD) technique can retrieve a subset of the wind field from a single ground-based Doppler radar under the assumption of nearly axisymmetric rotational wind, but is shown to have errors from aliasing of unresolved wind components.
    An improved technique that mitigates errors due to storm motion is derived in this study, although some spatial aliasing remains due to limited information content from the single Doppler measurements.
    A spline-based variational wind retrieval technique called SAMURAI can retrieve the full three-dimensional wind field from airborne radar fore-aft pseudo-dual Doppler scanning, but is shown to have errors due to temporal aliasing from the non-simultaneous Doppler measurements.
    A comparison between the two techniques shows that the axisymmetric tangential winds are generally comparable between the two techniques after the improvements to GVTD retrievals.
    Fourier decomposition of asymmetric kinematic and convective structure shows more discrepancies due to spatial and temporal aliasing in the retrievals.
    The advantages and disadvantages of each technique for studying tropical cyclone structure are discussed, and suggest that complementary information can be retrieved from both single and multiple Doppler retrievals.
    Future improvements to the asymmetric flow assumptions in single Doppler analysis and steady-state assumptions in pseudo-dual Doppler analysis are required to reconcile differences in retrieved tropical cyclone structure.
    </p>
      </center>
  </div>
  <div class="subcontent-2">
    <center> <h3>Plain Language Summary</h3> </center>
      <center>  
      <p class="align-justify">
    Polygonal eyewall asymmetries of Hurricane Michael (2018) during rapid intensification (RI) are analyzed from ground-based single Doppler radar. Here we present the first observational evidence of the evolving wind field of a polygonal eyewall during RI to Category 5 intensity by deducing the axisymmetric and asymmetric winds at 5-minute intervals. Spectral time decomposition of the retrieved tangential wind structure shows quantitative evidence of high-order azimuthal wavenumbers with propagation speeds that are consistent with linear wave theory on a radial vorticity gradient, suggesting the presence of rapidly-evolving vortex Rossby waves. Dual-Doppler winds from the airborne NOAA P-3 Hurricane Hunter provide further evidence of the three-dimensional vortex structure that supports growth of asymmetries during RI. Both reflectivity and tangential wind fields show polygonal structure and propagate at similar speeds, suggesting a close coupling of the dynamics and the convective organization during the intensification.  </p>
      </center>
  </div>

  <div class="button-wrap col-md-2">
    <a href="#" class="button">
      Abstract
    </a>
    <a href="#" class="button">
      Plain Language
    </a>

  </div>

</div>


  <div class="6u$ 12u$(medium)">
  <center> <h3>Key Figure</h3> </center>
    <center>
    <p class="image fit" style="width:85%">
    <a href="#"><img src="./Publications/figures/Cha_et_al_GRL_2020.png" alt="" /></a>  </p>
    </center>

    <center>
    <p class="align-justify">
    Spectral time decomposition of m = 1 - 4 (a) tangential wind components (b) reflectivity components. The derived propagation speeds of each (c) tangential wavenumber and (d) reflectivity wavenumber and the theoretical VRWs propagation speed from the linear wave theory. Figure is derived from Fig. 4 in Cha et al. 2020.
    </p>

    <ul class="actions align-center button-space">
      <li><a href="./Publications/papers/Cha_et_al_GRL_2020.pdf" class="button alt">PDF</a></li>
      <li><a href="#" class="button alt">BibTex</a></li>
    </ul>
    </center>
    </div>
</div>
---

<div class="12u$ 12u$(medium)">
  <ul class="actions fit">
    <li><a href="#" class="button special fit">Asymmetric Dynamics</a></li>
    <li><a href="#" class="button special fit">Radar</a></li>
    <li><a href="#" class="button special fit">TC case study</a></li>
  </ul>
</div>
