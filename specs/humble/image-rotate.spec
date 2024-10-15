# Meta Package
Name:           ros-humble-image-rotate
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_rotate/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-image_rotate and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_rotate
Requires:       ros2-humble-image_rotate-devel

Obsoletes: ros-humble-image-rotate < 3.0.5-1

%description
ROS humble package image_rotate.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
