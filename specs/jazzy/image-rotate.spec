# Meta Package
Name:           ros-jazzy-image-rotate
Version:        5.0.4
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_rotate/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-jazzy-image_rotate and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_rotate
Requires:       ros2-jazzy-image_rotate-devel

Obsoletes: ros-jazzy-image-rotate < 5.0.4-1

%description
ROS jazzy package image_rotate.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.4-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.3-1
- Update to latest release
