# Meta Package
Name:           ros-humble-image-view
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_view/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-image_view and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_view
Requires:       ros2-humble-image_view-devel

Obsoletes: ros-humble-image-view < 3.0.5-1

%description
A simple viewer for ROS image topics. Includes a specialized viewer
for stereo + disparity images.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
