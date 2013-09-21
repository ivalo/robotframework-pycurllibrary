Developer Guide
============================

Following instructions are for developers.

## Distribution

        python setup.py register
        python setup.py sdist upload

### Generate Keyword document

        python -m robot.libdoc src/PycURLLibrary index.html

Copy *index.html* into *gh-pages* branch and commit it and push it to the GitHub remote

### Generate Release Notes document

Edit pom.xml for correct release version, change *version* element to match GitHub Milestone:

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-changes-plugin</artifactId>
        <configuration>
          ...
          <version>0.9.4</version>
          ...
        </configuration>
      </plugin>

After right Milestone has been edited run following *Maven* command:

        mvn changes:announcement-generate

Result can be found from file *robotframework-pycurllibrary/target/announcement/announcement.vm*

Edit *RELEASE-NOTES.md* with nessessary copy paste.

## Unit testing

Start mock server:

        python test/testwebserver.py 53004


Run tests:

        pybot tests/acceptance/pycurllibrary_tests.txt
