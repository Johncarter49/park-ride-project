# FROM openjdk:12-alpine
# VOLUME /tmp
# ADD /build/libs/*.jar theme-park-ride-gradle.jar
# EXPOSE 8080
# ENTRYPOINT exec java -jar theme-park-ride-gradle.jar
# HEALTHCHECK --interval=5m --timeout=3s --retries=3 \
# CMD curl -f http://localhost:5000/ || exit 1

# build stage
FROM eclipse-temurin:8-jdk AS build
WORKDIR /workspace
COPY . .
RUN chmod +x ./gradlew && ./gradlew clean bootJar --no-daemon

# runtime stage
FROM eclipse-temurin:8-jre
WORKDIR /app
COPY --from=build /workspace/build/libs/*.jar app.jar

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:8080/actuator/health || exit 1

ENTRYPOINT ["java","-jar","/app/app.jar"]
