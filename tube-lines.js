//  `<script src="assets/tube-lines.js"></script>` at the top of <body>
// (where the inline <svg class="tube-lines"> used to be pasted on every
// page) — this writes that same markup in place, so it only lives here.
document.write(`
<svg class="tube-lines" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <filter id="tubeGlow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge>
        <feMergeNode in="b"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <linearGradient id="gGold" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0" spreadMethod="repeat">
      <stop class="stop-gold-a" offset="0%"/>
      <stop class="stop-gold-b" offset="50%"/>
      <stop class="stop-gold-a" offset="100%"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="320 0" dur="5s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="gCentral" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0" spreadMethod="repeat">
      <stop class="stop-central-a" offset="0%"/>
      <stop class="stop-central-b" offset="50%"/>
      <stop class="stop-central-a" offset="100%"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="320 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="gCircle" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0" spreadMethod="repeat">
      <stop class="stop-circle-a" offset="0%"/>
      <stop class="stop-circle-b" offset="50%"/>
      <stop class="stop-circle-a" offset="100%"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="320 0" dur="7s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="gDlr" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="320" y2="0" spreadMethod="repeat">
      <stop class="stop-dlr-a" offset="0%"/>
      <stop class="stop-dlr-b" offset="50%"/>
      <stop class="stop-dlr-a" offset="100%"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="320 0" dur="5.5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <path class="tube-line" style="animation-delay:.1s" stroke="url(#gGold)"    filter="url(#tubeGlow)" d="M -60,140 L 240,140 Q 300,140 342.4,182.4 L 457.6,297.6 Q 500,340 560,340 L 840,340 Q 900,340 942.4,297.6 L 1057.6,182.4 Q 1100,140 1160,140 L 1560,140"/>
  <path class="tube-line" style="animation-delay:.5s" stroke="url(#gCircle)" filter="url(#tubeGlow)" d="M -60,420 L 160,420 Q 220,420 262.4,377.6 L 377.6,262.4 Q 420,220 480,220 L 960,220 Q 1020,220 1062.4,262.4 L 1177.6,377.6 Q 1220,420 1280,420 L 1560,420"/>
  <path class="tube-line" style="animation-delay:.3s" stroke="url(#gCentral)" filter="url(#tubeGlow)" d="M -60,720 L 200,720 Q 260,720 302.4,677.6 L 417.6,562.4 Q 460,520 520,520 L 800,520 Q 860,520 902.4,562.4 L 1017.6,677.6 Q 1060,720 1120,720 L 1560,720"/>
  <path class="tube-line" style="animation-delay:.7s" stroke="url(#gDlr)"    filter="url(#tubeGlow)" d="M -60,860 L 280,860 Q 340,860 384.4,819.6 L 515.6,700.4 Q 560,660 620,660 L 880,660 Q 940,660 984.4,700.4 L 1115.6,819.6 Q 1160,860 1220,860 L 1560,860"/>
</svg>
`);
