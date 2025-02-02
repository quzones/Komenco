unmanagedBase := baseDirectory.value / "lib"


lazy val helloWorldKomencoNative = project
  .in(file("."))
  .settings(
    name := "HelloWorldKomencoNative",
    libraryDependencies ++= Seq(
      "org.scala-lang" %% "toolkit" % "0.1.7",
      "org.scala-lang" %% "toolkit-test" % "0.1.7" % Test
    )
  )

