# Meta Package
Name:           ros-jazzy-tracetools-image-pipeline
Version:        5.0.9
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tracetools_image_pipeline and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tracetools_image_pipeline
Requires:       ros2-jazzy-tracetools_image_pipeline-devel

Obsoletes: ros-jazzy-tracetools-image-pipeline < 5.0.9-1

%description
LTTng tracing provider wrapper for image_pipeline ROS 2 meta-package.

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
