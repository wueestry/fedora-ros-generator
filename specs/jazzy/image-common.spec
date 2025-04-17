# Meta Package
Name:           ros-jazzy-image-common
Version:        5.1.6
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_common
Summary:        Meta package for ros2-jazzy-image_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_common
Requires:       ros2-jazzy-image_common-devel

Obsoletes: ros-jazzy-image-common < 5.1.6-1

%description
Common code for working with images in ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 17 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.6-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.5-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.4-1
- Update to latest release
