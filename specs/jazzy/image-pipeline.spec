# Meta Package
Name:           ros-jazzy-image-pipeline
Version:        5.0.9
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_pipeline/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-jazzy-image_pipeline and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_pipeline
Requires:       ros2-jazzy-image_pipeline-devel

Obsoletes: ros-jazzy-image-pipeline < 5.0.9-1

%description
image_pipeline fills the gap between getting raw images from a camera
driver and higher-level vision processing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Mar 14 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.9-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.6-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.5-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.4-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.3-1
- Update to latest release
