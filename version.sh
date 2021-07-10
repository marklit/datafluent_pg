git tag -a $(cat VERSION) -m 'Release v$(cat VERSION)' main
git push --tags
