# DevOps Akışı (Adım Adım) - Theme Park Ride

Bu doküman, projedeki DevOps akışını ve `dev/prod` profillerinin nasıl çalıştığını kısa ve operasyonel şekilde özetler.

## 1) Uygulama konfigürasyonu nasıl ayrılıyor?
1. Ortak ayarlar `application.yml` içinde tanımlıdır (port varsayılanı `5000`).
2. Ortama özel farklar profile dosyalarından gelir:
   - `application-dev.yml`: H2 console açık, actuator endpoint'leri geniş.
   - `application-prod.yml`: H2 console kapalı, actuator kısıtlı (`health/info/prometheus`).
3. Docker Compose ile `env/dev.env` veya `env/prod.env` yüklenir ve `SPRING_PROFILES_ACTIVE` belirlenir.

## 2) Local çalıştırma (Docker Compose)
### Dev
```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```
- Container içinde app yine `5000` portunda çalışır.
- Host tarafında `5001:5000` map edilir.
- Beklenen erişim: `http://localhost:5001/ride`

### Prod
```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
- Container içinde app `5000` portunda.
- Host tarafında `5000:5000` map edilir.
- Beklenen erişim: `http://localhost:5000/ride`

> Not: Compose tarafında TLS terminate eden bir reverse proxy tanımlı değil. Bu yüzden doğrudan `https://...:5000` veya `https://...:5001` kullanımı normalde başarısız olur.

## 3) CI/CD akışı (Jenkinsfile)
1. **Build**: `./gradlew clean build`
2. **Unit Tests**: `./gradlew test`
3. **Docker Build**: image oluşturulur.
4. **Deploy Dev (auto)**: dev compose ile otomatik ayağa kaldırılır.
5. **Deploy Prod (manual)**: insan onayı (`input`) sonrası prod compose çalışır.
6. **Kubernetes kontrol adımı**: credential ile `kubectl get nodes`.

## 4) Kubernetes/Helm tarafı
- Helm chart `deployment/charts/theme-park-ride` altında.
- Service tipi NodePort (`30085`) ve Ingress host örneği `mykube.freeddns.org` olarak duruyor.
- Ingress şablonunda host için `TODO` notu bulunuyor; gerçek DNS ve TLS ayarı yapılmadıysa dış erişim sorunlu olabilir.

## 5) Verdiğiniz URL'ler neden çalışmıyor olabilir?
`https://62.210.91.191:5001` ve `https://62.210.91.191:5000` için olası nedenler:
1. **HTTP/HTTPS uyumsuzluğu**: Compose servisleri plain HTTP verir; HTTPS beklemek hatalı olabilir.
2. **Servis gerçekten ayakta değil**: container down olabilir.
3. **Port/firewall kapalı**: 5000/5001 dışarı açılmamış olabilir.
4. **Yanlış endpoint**: root `/` yerine `/ride` veya `/actuator/health` denenmeli.
5. **Ters proxy/ingress gereksinimi**: TLS için Nginx/Traefik + sertifika gerekebilir.

## 6) Hızlı teşhis komutları
```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml ps
docker compose -f docker-compose.yml -f docker-compose.prod.yml ps
docker compose -f docker-compose.yml -f docker-compose.dev.yml logs --tail=200
docker compose -f docker-compose.yml -f docker-compose.prod.yml logs --tail=200
curl -i http://localhost:5001/actuator/health
curl -i http://localhost:5000/actuator/health
curl -i http://localhost:5001/ride
curl -i http://localhost:5000/ride
```
