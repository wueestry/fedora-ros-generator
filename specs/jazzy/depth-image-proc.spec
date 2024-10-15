# Meta Package
Name:           ros-jazzy-depth-image-proc
Version:        5.0.4
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/depth_image_proc/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-jazzy-depth_image_proc and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-depth_image_proc
Requires:       ros2-jazzy-depth_image_proc-devel

Obsoletes: ros-jazzy-depth-image-proc < 5.0.4-1

%description
Contains components for processing depth images such as those produced
by OpenNI camera. Functions include creating disparity images and
point clouds, as well as registering (reprojecting) a depth image into
another camera frame.

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
