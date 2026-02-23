# Proje Gereksinim Haritası (TR)

Bu doküman, mevcut repoyu verilen "Project Requirements & Expectations" listesine göre hızlıca değerlendirir ve tamamlamak için bir yol haritası önerir.

## 1) Dockerize Your Application
**Durum:** ✅ Büyük ölçüde tamam.
- Multi-stage `Dockerfile` var (build + runtime).  
- Compose ile çalıştırma var.  
- Registry kullanımına dair kanıt var (GitLab registry image örneği).

**İyileştirme:**
- CI pipeline içinde image'ı her build'de registry'ye push eden adımı netleştir/dokümante et.

## 2) Dev & Prod Çoklu Ortam
**Durum:** ✅ Tamam.
- `docker-compose.dev.yml` ve `docker-compose.prod.yml` ayrımı var.
- `env/dev.env` ve `env/prod.env` ayrımı var.
- CI'da dev otomatik, prod manuel onaylı deploy akışı var.

## 3) Testler
**Durum:** ⚠️ Kısmen tamam.
- JUnit/Spring testleri mevcut.
- Jenkins'te `./gradlew test` var.

**Eksik/Geliştirme:**
- Test kapsamı ölçümü (Jacoco) eklenebilir.
- Integration/API/E2E testlerinden en az bir katman eklemek projeyi güçlendirir.

## 4) Kubernetes ile Orkestrasyon
**Durum:** ✅ Tamam (Helm ile).
- Helm chart içinde Deployment/Service/Ingress mevcut.

**Eksik/Geliştirme:**
- ConfigMap/Secret manifestleri görünür değil; eklenmeli.
- Namespace bazlı dev/prod ayrımı ve değer dosyalarıyla net akış dokümante edilmeli.

## 5) CI/CD Pipeline
**Durum:** ✅ Tamam.
- Jenkinsfile ile build/test/docker/deploy adımları var.
- Prod deploy için onay kapısı var.

**İyileştirme:**
- Branch stratejisi ve release tagging açıkça belgelensin.
- Registry push ve Kubernetes deploy adımları tek bir tutarlı pipeline tasarımında birleştirilsin.

## 6) Monitoring (Prometheus + Grafana / Datadog)
**Durum:** ❌ Henüz yok.
- Kod tabanında Prometheus/Grafana kurulumuna dair manifest, compose servisi veya dashboard provizyonu görünmüyor.
- Actuator bağımlılığı var ama tek başına Prometheus+Grafana kurulumu anlamına gelmez.

## 7) Security (DevSecOps)
**Durum:** ⚠️ Kısmen.
- CI/CD'de credential kullanımı mevcut.

**Eksik:**
- En az 3 güvenlik maddesi net olarak uygulanmalı:
  1. Container image tarama (örn. Trivy)
  2. Dependency scanning (Dependabot/Snyk)
  3. Secret yönetimi (K8s Secret + external secret manager)
  4. HTTPS ingress + cert-manager
  5. (Bonus) RBAC

## 8) Disaster Recovery
**Durum:** ❌ Eksik.
- Yedekleme/geri yükleme prosedürü ve rollback senaryoları dokümante edilmemiş görünüyor.

## 9) Dokümantasyon + Mimari Diyagram
**Durum:** ⚠️ Kısmen.
- README'ler var.
- Ancak gereksinimde geçen kapsamlı dokümantasyon (monitoring, security, DR, architecture diagram) tek yerde tam değil.

---

## Terraform IaC Eklenmeli mi?
**Kısa cevap:** Zorunlu değil ama **çok önerilir**.

Bu gereksinim setinde Terraform adı zorunlu geçmiyor; Kubernetes manifest/Helm ile deployment şartı zaten sağlanabiliyor. Ancak gerçek hayat simülasyonu ve "infrastructure redeploy from IaC" beklentisi için Terraform eklemek projeyi ciddi şekilde güçlendirir.

**Ne için kullanabilirsin?**
- Cloud altyapısı (VPC/network, K8s cluster, node pool)
- Registry/iam/policy kaynakları
- Monitoring stack altyapısı

**Öneri:**
- Eğer zamanın varsa Terraform ekle ve README'de "infra bring-up" + "destroy/recreate" adımlarını yaz.

---

## 2 Haftalık Pratik Yol Haritası
1. **Monitoring ekle (öncelik 1):** kube-prometheus-stack veya Prometheus+Grafana manifest/helm kur. En az 1 dashboard + 1 alert koy.
2. **Security hardening (öncelik 1):** Trivy scan'ı pipeline'a ekle; Dependabot/Snyk aç; secret'ları env yerine secret store'a taşı.
3. **DR dokümanı (öncelik 2):** backup/restore ve rollback runbook yaz.
4. **K8s konfigürasyonlarını tamamla (öncelik 2):** ConfigMap + Secret + namespace stratejisi.
5. **Terraform (öncelik 3 ama değerli):** en az cluster/namespace/registry için temel modül koy.
6. **Dokümantasyon tekilleştirme:** ana README'ye tüm akışları (dev/prod, CI/CD, monitoring, security, DR, mimari diyagram) bağla.

---

## "Her şey tamam mı?" için net cevap
Bugünkü repoya göre: **Henüz tam değil.**  
Özellikle monitoring (Prometheus/Grafana), DR planı, ve güvenlik maddelerinin en az 3 tanesinin açık/kanıtlı uygulanması tarafında boşluk var. Bu maddeleri kapattığında "tamam" diyebilirsin.
