# Meta Package
Name:           ros-humble-image-common
Version:        3.1.9
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/image_common
Summary:        Meta package for ros2-humble-image_common and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_common
Requires:       ros2-humble-image_common-devel

Obsoletes: ros-humble-image-common < 3.1.9-1

%description
Common code for working with images in ROS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.9-1
- Update to latest release
