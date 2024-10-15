# Meta Package
Name:           ros-jazzy-image-proc
Version:        5.0.4
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/image_proc/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-jazzy-image_proc and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_proc
Requires:       ros2-jazzy-image_proc-devel

Obsoletes: ros-jazzy-image-proc < 5.0.4-1

%description
Single image rectification and color processing.

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
