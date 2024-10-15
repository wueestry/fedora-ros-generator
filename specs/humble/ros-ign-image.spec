# Meta Package
Name:           ros-humble-ros-ign-image
Version:        0.244.15
Release:        1%{?dist}
License:        Apache 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-ros_ign_image and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-ros_ign_image
Requires:       ros2-humble-ros_ign_image-devel

Obsoletes: ros-humble-ros-ign-image < 0.244.15-1

%description
Shim package to redirect to ros_gz_image.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.244.15-1
- Update to latest release
