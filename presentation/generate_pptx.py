from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape
import datetime

slides = [
    ("Theme Park Ride Service DevOps Project Overview", [
        "English Project Presentation",
        "Spring Boot • Docker • CI/CD • Monitoring",
    ]),
    ("1) Project Purpose & Scope", [
        "Build a reliable backend service for theme park ride management.",
        "Demonstrate a full DevOps lifecycle: build, package, deploy, observe.",
        "Support environment-aware deployment with clear dev/prod separation.",
    ]),
    ("2) Technology Stack", [
        "Java + Spring Boot (REST API + Actuator metrics).",
        "Gradle build system for compilation, tests, and packaging.",
        "Docker + Docker Compose for local and environment-specific runtime.",
        "Prometheus + Grafana for metrics collection and visualization.",
        "Jenkins pipeline and Helm chart artifacts for CI/CD and Kubernetes deployment.",
    ]),
    ("3) Application Architecture", [
        "Layered Spring Boot structure.",
        "Controller layer exposes ride management endpoints.",
        "Model and repository manage ride data persistence.",
        "Configuration profiles tune behavior per environment.",
        "Actuator endpoints provide health checks and Prometheus metrics.",
    ]),
    ("4) Environment Strategy (Dev vs Prod)", [
        "Development profile (dev): H2 console enabled, all actuator endpoints, port 5001.",
        "Production profile (prod): H2 console disabled, limited actuator endpoints, port 5000.",
        "Production data persists using mounted volume at /data.",
    ]),
    ("5) Containerization & Local Run", [
        "Single base docker-compose.yml with environment-specific overrides.",
        "Development run: docker-compose + docker-compose.dev.yml.",
        "Production run: docker-compose + docker-compose.prod.yml.",
        "Environment variables loaded from env/dev.env and env/prod.env.",
    ]),
    ("6) Observability & Monitoring", [
        "Monitoring stack includes Prometheus and Grafana.",
        "Service health endpoint: /actuator/health.",
        "Metrics endpoint: /actuator/prometheus.",
        "Prometheus UI: localhost:9090, Grafana UI: localhost:3000.",
    ]),
    ("7) CI/CD Pipeline & Release Flow", [
        "Development (review) deployment runs automatically.",
        "Production deployment requires manual approval.",
        "Pipeline artifacts support Helm-based Kubernetes deployment.",
        "Approach balances speed in dev and control in prod.",
    ]),
    ("8) Security & Operational Practices", [
        "Sensitive and debug endpoints are restricted in production profile.",
        "Separate environment variable files for dev and prod.",
        "Persistent storage prevents data loss on restart.",
        "Health and metrics support proactive incident response.",
    ]),
    ("9) Roadmap / Next Improvements", [
        "Add integration and contract tests.",
        "Introduce secret management (Vault/KMS).",
        "Harden API with authentication and rate limiting.",
        "Expand dashboard KPIs (error rate, latency percentile, saturation).",
    ]),
    ("10) Conclusion", [
        "Project demonstrates practical DevOps readiness around a Spring service.",
        "Delivers consistent deployment, visibility, and operational control.",
        "Ready to scale with additional automation and production hardening.",
        "Thank you! Questions?",
    ]),
]

def slide_xml(title, bullets):
    paras = [f'<a:p><a:r><a:rPr lang="en-US" sz="3600" b="1"/><a:t>{escape(title)}</a:t></a:r></a:p>', '<a:p><a:endParaRPr lang="en-US"/></a:p>']
    for b in bullets:
        paras.append(f'<a:p><a:pPr lvl="0" marL="342900" indent="-171450"><a:buChar char="•"/></a:pPr><a:r><a:rPr lang="en-US" sz="2200"/><a:t>{escape(b)}</a:t></a:r></a:p>')
    paras_xml = ''.join(paras)
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr><p:sp><p:nvSpPr><p:cNvPr id="2" name="TextBox 1"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="274320"/><a:ext cx="8229600" cy="5943600"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr><p:txBody><a:bodyPr wrap="square" rtlCol="0" anchor="t"/><a:lstStyle/>{paras_xml}</p:txBody></p:sp></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>'''

out_dir = Path('presentation')
out_dir.mkdir(exist_ok=True)
out = out_dir / 'Theme_Park_DevOps_Presentation_EN.pptx'
now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

with ZipFile(out, 'w', ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/><Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/><Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/><Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>{''.join([f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' for i in range(1, len(slides)+1)])}</Types>''')
    z.writestr('_rels/.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>')
    z.writestr('docProps/core.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Theme Park DevOps Presentation</dc:title><dc:creator>Codex</dc:creator><cp:lastModifiedBy>Codex</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified></cp:coreProperties>')
    z.writestr('docProps/app.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office PowerPoint</Application><Slides>{len(slides)}</Slides><Notes>0</Notes><HiddenSlides>0</HiddenSlides><MMClips>0</MMClips><ScaleCrop>false</ScaleCrop><Company></Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc><HyperlinksChanged>false</HyperlinksChanged><AppVersion>16.0000</AppVersion></Properties>')

    slide_ids = ''.join([f'<p:sldId id="{256+i}" r:id="rId{2+i}"/>' for i in range(len(slides))])
    z.writestr('ppt/presentation.xml', f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst><p:sldIdLst>{slide_ids}</p:sldIdLst><p:sldSz cx="9144000" cy="6858000" type="screen4x3"/><p:notesSz cx="6858000" cy="9144000"/><p:defaultTextStyle/></p:presentation>')
    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    rels += [f'<Relationship Id="rId{2+i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i+1}.xml"/>' for i in range(len(slides))]
    rels.append('</Relationships>')
    z.writestr('ppt/_rels/presentation.xml.rels', ''.join(rels))
    z.writestr('ppt/slideMasters/slideMaster1.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:bg><p:bgRef idx="1001"><a:schemeClr val="bg1"/></p:bgRef></p:bg><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/><p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst><p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles></p:sldMaster>')
    z.writestr('ppt/slideMasters/_rels/slideMaster1.xml.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>')
    z.writestr('ppt/slideLayouts/slideLayout1.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1"><p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>')
    z.writestr('ppt/slideLayouts/_rels/slideLayout1.xml.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>')
    z.writestr('ppt/theme/theme1.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme"><a:themeElements><a:clrScheme name="Office"><a:dk1><a:srgbClr val="000000"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="1F497D"/></a:dk2><a:lt2><a:srgbClr val="EEECE1"/></a:lt2><a:accent1><a:srgbClr val="4F81BD"/></a:accent1><a:accent2><a:srgbClr val="C0504D"/></a:accent2><a:accent3><a:srgbClr val="9BBB59"/></a:accent3><a:accent4><a:srgbClr val="8064A2"/></a:accent4><a:accent5><a:srgbClr val="4BACC6"/></a:accent5><a:accent6><a:srgbClr val="F79646"/></a:accent6><a:hlink><a:srgbClr val="0000FF"/></a:hlink><a:folHlink><a:srgbClr val="800080"/></a:folHlink></a:clrScheme><a:fontScheme name="Office"><a:majorFont><a:latin typeface="Calibri"/></a:majorFont><a:minorFont><a:latin typeface="Calibri"/></a:minorFont></a:fontScheme><a:fmtScheme name="Office"><a:fillStyleLst/><a:lnStyleLst/><a:effectStyleLst/><a:bgFillStyleLst/></a:fmtScheme></a:themeElements></a:theme>')

    for i, (title, bullets) in enumerate(slides, start=1):
        z.writestr(f'ppt/slides/slide{i}.xml', slide_xml(title, bullets))
        z.writestr(f'ppt/slides/_rels/slide{i}.xml.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>')

print(f'Created {out}')
