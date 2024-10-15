# Meta Package
Name:           ros-humble-image-pipeline
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_pipeline/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-image_pipeline and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_pipeline
Requires:       ros2-humble-image_pipeline-devel

Obsoletes: ros-humble-image-pipeline < 3.0.5-1

%description
image_pipeline fills the gap between getting raw images from a camera
driver and higher-level vision processing.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
